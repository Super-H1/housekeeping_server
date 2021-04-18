from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from collect.models import Collect
from collect.serializers import CollectSerializer
from utils.redis_set import Res


class CollectViewset(ModelViewSet):
    queryset = Collect.objects.filter(is_collect=True).order_by('-creation_time')
    serializer_class = CollectSerializer
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        if not serializers.is_valid():
            return JsonResponse(data={'message': '数据错误'}, status=400)
        user_id = Res.get('user_id').decode('utf-8')
        instance = serializers.create(serializers.validated_data, user_id)
        return JsonResponse(data={'flag': True, 'result': {'message': 'success'}}, status=200)
