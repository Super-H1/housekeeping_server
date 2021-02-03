from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from category.models import Category
from service.serializers import ServicesSerializer
from user.models import Services, UserInfo, Cart


class ServiceViewset(ModelViewSet):
    queryset = Services.objects.all().order_by('-creation_time')
    serializer_class = ServicesSerializer
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('userid')
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(data={'message': '数据错误'}, status=400)
        service_obj = serializer.create(serializer.validated_data)
        user = UserInfo.objects.filter(id=user_id).first()
        if not user:
            return JsonResponse(data={'message': '该用户不存在'}, status=400)
        user.service.add(service_obj)
        user.save()
        result = self.get_serializer(service_obj)
        return JsonResponse(data={'flag': True, 'result': result.data}, status=200)

    def list(self, request):
        id = request.query_params.get('pk', None)
        user_id = request.query_params.get('user_id', None)
        queryset = self.get_queryset()
        if id:
            queryset = Services.objects.filter(category_id=id).order_by('-creation_time')
        result = self.get_serializer(queryset, many=True)
        resultData = result.data
        for res in resultData:
            category = Category.objects.filter(id=res['category_id']).first()
            cart_good = Cart.objects.filter(user_id=user_id, good_id=res['id']).order_by('-creation_time').first()
            res['price'] = 'NA'
            res['good_num'] = 0
            if category:
                res['category_name'] = category.name
                res['price'] = category.price
                if res['grade'] > 1:
                    res['price'] = res['grade'] * category.price * 0.85
            if cart_good:
                res['good_num'] = cart_good.good_num
        return JsonResponse(data=resultData, status=200, safe=False)
