from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from address.models import Address
from address.serializers import AddressSerializer


class AddressViewset(ModelViewSet):
    queryset = Address.objects.all().order_by('-creation_time')
    serializer_class = AddressSerializer
    lookup_field = 'pk'

    def create(self, request):
        serializers = self.get_serializer(data=request.data)
        user = request.session.get('user')
        if not user:
            return JsonResponse(data={'message': '用户未登录!'}, status=400)
        if not serializers.is_valid():
            return JsonResponse(data={'message': '数据错误'}, status=400)
        address_obj = serializers.create(serializers.validated_data, user)
        result = self.get_serializer(address_obj)
        return JsonResponse(data={'flag': True, 'result': result.data}, status=200)

    def list(self, request):
        user = request.session.get('user')
        if not user:
            return JsonResponse(data={'message': '用户未登录!'}, status=400)
        queryset = self.get_queryset().filter(user_id=user.id)
        serializer = self.get_serializer(queryset, many=True)
        result = serializer.data
        return JsonResponse(data={'flag': True, 'data': result}, status=200)

    def destroy(self, request, pk):
        instance = self.get_queryset().filter(id=pk).first()
        if not instance:
            return JsonResponse(data={'message': '数据错误'}, status=400)
        instance.delete()
        return JsonResponse(data=None, status=200, safe=False)

