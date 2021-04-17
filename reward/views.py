from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from reward.models import Reward
from reward.serializers import RewardSerializer


class RewardViewset(ModelViewSet):
    queryset = Reward.objects.filter(is_grant=False).order_by('-creation_time')
    serializer_class = RewardSerializer
    lookup_field = 'pk'

    @action(methods=['post'], detail=False)
    def release_reward(self, request):
        id = request.data.get('id')
        queryset = self.get_queryset()
        instance = queryset.filter(id=id).first()
        money = None
        if instance:
            instance.total_money += instance.money
            instance.is_grant = True
            instance.money = 0
            instance.save()
            money = instance.total_money
        data = {'money': money}
        return JsonResponse(data={'flag': True, 'result': data}, status=200)

