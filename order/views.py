from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from order.models import Order, OrderService
from order.serializers import OrderSerializer, OrderServiceSerializer
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
        if not user_id:
            return JsonResponse(data=None, status=200, safe=False)
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



