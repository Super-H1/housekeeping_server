from rest_framework import serializers

from reward.models import Reward
from user.serializers import UserSerializer


class RewardSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Reward
        fields = '__all__'
