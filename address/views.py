from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from address.models import Address
from address.serializers import AddressSerializer, AddressDefaultSerializer
from utils.redis_set import Res


class AddressViewset(ModelViewSet):
    queryset = Address.objects.all().order_by('-creation_time')
    serializer_class = AddressSerializer
    lookup_field = 'pk'

    def create(self, request):
        serializers = self.get_serializer(data=request.data)
        user_id = Res.get('user_id').decode('utf-8')
        if not user_id:
            return JsonResponse(data={'message': '用户未登录!'}, status=400)
        if not serializers.is_valid():
            return JsonResponse(data={'message': '数据错误'}, status=400)
        address_obj = serializers.create(serializers.validated_data, user_id)
        result = self.get_serializer(address_obj)
        return JsonResponse(data={'flag': True, 'result': result.data}, status=200)

    def update(self, request, pk):
        user_id = Res.get('user_id').decode('utf-8')
        if not user_id:
            return JsonResponse(data={'message': '用户未登录!'}, status=400)
        instance = self.get_queryset().filter(id=pk).first()
        if not instance:
            return JsonResponse(data={'message': '该地址不存在!'}, status=400)
        serializers = self.get_serializer(data=request.data)
        if not serializers.is_valid():
            return JsonResponse(data={'message': '数据错误'}, status=400)
        address_obj = serializers.update(instance, serializers.validated_data)
        result = self.get_serializer(address_obj)
        return JsonResponse(data={'flag': True, 'result': result.data}, status=200)

    def list(self, request):
        user_id = Res.get('user_id').decode('utf-8')
        if not user_id:
            return JsonResponse(data={'message': '用户未登录!'}, status=400)
        queryset = self.get_queryset().filter(user_id=user_id)
        serializer = self.get_serializer(queryset, many=True)
        result = serializer.data
        return JsonResponse(data={'flag': True, 'data': result}, status=200)

    def destroy(self, request, pk):
        instance = self.get_queryset().filter(id=pk).first()
        if not instance:
            return JsonResponse(data={'message': '该地址不存在!'}, status=400)
        instance.delete()
        return JsonResponse(data=None, status=200, safe=False)

    # def retrieve(self, request, pk):
    #     if not pk:
    #         return JsonResponse(data={'message': '该地址不存在!'}, status=400)
    #     instance = self.get_queryset().filter(id=pk).first()
    #     serializer = self.get_serializer(instance)
    #     result = serializer.data
    #     return JsonResponse(data={'flag': True, 'data': result}, status=200)

    @action(methods=['post'], detail=True, url_path='set_default_address', url_name='set_default_address')
    def set_default_address(self, request):
        '''
        设置默认地址
        '''
        user_id = Res.get('user_id').decode('utf-8')
        if not user_id:
            return JsonResponse(data={'message': '用户未登录!'}, status=400)
        serializers = AddressDefaultSerializer(data=request.data)
        if not serializers.is_valid():
            return JsonResponse(data={'message': '数据错误'}, status=400)
        queryset = self.get_queryset().filter(user_id=user_id)
        instance = serializers.set_default_address(queryset, serializers.validated_data)
        result = self.get_serializer(instance)
        return JsonResponse(data={'flag': True, 'result': result.data}, status=200)

    @action(methods=['get'], detail=False, url_path='get_default_address', url_name='get_default_address')
    def get_default_address(self, request):
        '''
        获取默认地址
        :param request:
        :return:
        '''
        user_id = Res.get('user_id').decode('utf-8')
        if not user_id:
            return JsonResponse(data={'message': '用户未登录!'}, status=400)
        instance = self.get_queryset().filter(user_id=user_id, is_default=True).first()
        result = self.get_serializer(instance)
        return JsonResponse(data={'flag': True, 'result': result.data}, status=200)

