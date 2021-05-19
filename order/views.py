from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from comment.models import Comment
from order.logics import add_reward_to_user, complain_deductions
from order.models import Order, OrderService
from order.serializers import OrderSerializer, OrderServiceSerializer
from service.models import Services
from user.models import UserInfo
from utils.custom_enum import OrderStatus
from utils.redis_set import Res


class OrderViewset(ModelViewSet):
    queryset = Order.objects.all().order_by('-creation_time')
    serializer_class = OrderSerializer
    lookup_field = 'pk'

    def create(self, request):
        serializers = self.get_serializer(data=request.data)
        user_id = Res.get('user_id').decode('utf-8')
        if not user_id:
            return JsonResponse(data={'message': '用户未登录!'}, status=400)
        if not serializers.is_valid():
            return JsonResponse(data={'message': '数据错误'}, status=400)
        order_obj = serializers.create(serializers.validated_data, user_id)
        order_service_obj = OrderService.objects.filter(order=order_obj)
        result = OrderServiceSerializer(order_service_obj, many=True)
        data = {}
        service_list = []
        for item in result.data:
            data['order'] = item['order']
            item['service']['o_service_num'] = item['o_service_num']
            item['service']['service_price'] = item['service_price']
            service_list.append(item['service'])
        data['service'] = service_list
        return JsonResponse(data={'flag': True, 'result': data}, status=200)

    def list(self, request):
        user_id = request.query_params.get('user_id', None)
        type = request.query_params.get('type', None)
        orders = []
        if not user_id:
            orders = self.get_queryset().filter(
                status__in=[OrderStatus.AdminCheck.value, OrderStatus.Refund.value, OrderStatus.ComplainOrder.value])
        else:
            if user_id:
                if type:
                    user = UserInfo.objects.filter(id=user_id).first()
                    services = user.service.all()
                    orders = []
                    for ser in services:
                        orderservices = OrderService.objects.filter(service_id=ser.id)
                        for s in orderservices:
                            order = s.order
                            if order.status == OrderStatus.Paid.value or order.status == OrderStatus.Accept.value:
                                orders.append(order)
                else:
                    orders = self.get_queryset().filter(user_id=user_id)
        data_list = []
        for order in orders:
            order_service_obj = OrderService.objects.filter(order=order)
            result = OrderServiceSerializer(order_service_obj, many=True)
            data = {}
            service_list = []
            for item in result.data:
                data['order'] = item['order']
                item['service']['o_service_num'] = item['o_service_num']
                item['service']['service_price'] = item['service_price']
                service_list.append(item['service'])
            data['service'] = service_list
            data_list.append(data)
        return JsonResponse(data={'flag': True, 'data': data_list}, status=200)

    def retrieve(self, request, pk):
        instance = self.get_object()
        order_service_obj = OrderService.objects.filter(order=instance)
        result = OrderServiceSerializer(order_service_obj, many=True)
        data = {}
        service_list = []
        for item in result.data:
            data['order'] = item['order']
            item['service']['o_service_num'] = item['o_service_num']
            item['service']['service_price'] = item['service_price']
            service_list.append(item['service'])
        data['service'] = service_list
        return JsonResponse(data={'flag': True, 'result': data}, status=200)

    @action(methods=['post'], detail=False)
    def pay_order(self, request):
        '''
        付款
        :param request:
        :return:
        '''
        id = request.data.get('id')
        instance = Order.objects.filter(id=id).first()
        if instance:
            instance.status = OrderStatus.AdminCheck.value
            instance.save()
        return JsonResponse(data={'flag': True, 'result': None}, status=200)

    @action(methods=['post'], detail=False)
    def confirm_pay(self, request):
        '''
        管理员确认付款
        :param request:
        :return:
        '''
        id = request.data.get('id')
        instance = Order.objects.filter(id=id).first()
        if instance:
            instance.status = OrderStatus.Paid.value
            instance.save()
        return JsonResponse(data={'flag': True, 'result': None}, status=200)

    @action(methods=['post'], detail=False)
    def servicer_accept_order(self, request):
        '''
        服务人员接受订单
        :param request:
        :return:
        '''
        id = request.data.get('id')
        instance = Order.objects.filter(id=id).first()
        if instance:
            instance.status = OrderStatus.Accept.value
            instance.save()
        return JsonResponse(data={'flag': True, 'result': None}, status=200)

    @action(methods=['post'], detail=False)
    def servicer_refuse_order(self, request):
        '''
        服务人员拒绝订单
        :param request:
        :return:
        '''
        id = request.data.get('id')
        reason = request.data.get('reason', None)
        instance = Order.objects.filter(id=id).first()
        if instance:
            instance.status = OrderStatus.Refuse.value
            if reason:
                instance.remark = reason
            instance.save()
        return JsonResponse(data={'flag': True, 'result': None}, status=200)

    @action(methods=['post'], detail=False)
    def servicer_complete_order(self, request):
        '''
        服务人员确认完成订单
        :param request:
        :return:
        '''
        id = request.data.get('id')
        instance = Order.objects.filter(id=id).first()
        if instance:
            instance.status = OrderStatus.ServiceComplete.value
            instance.save()
        return JsonResponse(data={'flag': True, 'result': None}, status=200)

    @action(methods=['post'], detail=False)
    def user_confirm_complete_order(self, request):
        '''
        用户确认完成订单
        :param request:
        :return:
        '''
        id = request.data.get('id')
        instance = Order.objects.filter(id=id).first()
        if instance:
            instance.status = OrderStatus.UserOrderComplete.value
            instance.save()
            # 添加赏金记录
            add_reward_to_user(instance)
        return JsonResponse(data={'flag': True, 'result': None}, status=200)

    @action(methods=['post'], detail=False)
    def user_refund(self, request):
        '''
        用户申请退款
        :param request:
        :return:
        '''
        id = request.data.get('id')
        instance = Order.objects.filter(id=id).first()
        if instance:
            instance.status = OrderStatus.Refund.value
            instance.save()
            # 添加赏金记录
            add_reward_to_user(instance)
        return JsonResponse(data={'flag': True, 'result': None}, status=200)

    @action(methods=['post'], detail=False)
    def admin_agree_refund(self, request):
        '''
        管理员同意退款
        :param request:
        :return:
        '''
        id = request.data.get('id')
        instance = Order.objects.filter(id=id).first()
        if instance:
            instance.status = OrderStatus.OrderRefundSuccess.value
            instance.save()
            # 添加赏金记录
            add_reward_to_user(instance)
        return JsonResponse(data={'flag': True, 'result': None}, status=200)

    @action(methods=['post'], detail=False)
    def admin_agree_complain(self, request):
        '''
        管理员同意投诉
        :param request:
        :return:
        '''
        service_id = request.data.get('service_id')
        service = Services.objects.filter(id=service_id).first()
        if service:
            user = service.userinfo_set.all().first()
            # 添加赏金记录
            complain_deductions(user)
        return JsonResponse(data={'flag': True, 'result': None}, status=200)
