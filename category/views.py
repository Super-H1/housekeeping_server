from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from category.models import Category
from category.serializers import CategorySerializer


class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all().order_by('-creation_time')
    serializer_class = CategorySerializer
    lookup_field = 'pk'
    def create(self, request):
        serializers = self.get_serializer(data=request.data)
        if not serializers.is_valid():
            return JsonResponse(data={'message': '数据错误'}, status=400)
        category_obj = serializers.create(serializers.validated_data)
        result = self.get_serializer(category_obj)
        return JsonResponse(data={'flag': True, 'result': result.data}, status=200)


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        result = self.get_serializer(queryset, many=True)
        return JsonResponse(data=result.data, status=200, safe=False)

