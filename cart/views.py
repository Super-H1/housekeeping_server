from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from cart.models import Cart
from cart.serializers import CartSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all().order_by('-creation_time')
    serializer_class = CartSerializer
    lookup_field = 'pk'

    def create(self, request):
        serilaizer = self.get_serializer(data=request.data)
        if not serilaizer.is_valid():
            return JsonResponse(data={'message': '数据错误'}, status=400)
        cart_obj = serilaizer.create(serilaizer.validated_data)
        if not cart_obj:
            return JsonResponse(data=None, status=200, safe=False)
        result = self.get_serializer(cart_obj)
        return JsonResponse(data={'flag': True, 'result': result.data}, status=200)

    def list(self, request):
        user_id = request.query_params.get('user_id', None)
        if not user_id:
            return JsonResponse(data=None, status=200, safe=False)
        queryset = self.get_queryset().filter(user_id=user_id)
        serializer = self.get_serializer(queryset, many=True)
        result = serializer.data
        return JsonResponse(data={'flag': True, 'data': result}, status=200)

    def destroy(self, request, pk):
        instance = self.get_queryset().filter(id=pk).first()
        if not instance:
            return JsonResponse(data={'message': '数据错误'}, status=400)
        instance.delete()
        return JsonResponse(data=None, status=200, safe=False)
