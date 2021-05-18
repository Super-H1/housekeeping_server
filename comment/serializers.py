from rest_framework import serializers

from comment.models import Comment
from utils.common_utils import get_model_fields


class CommentSerializer(serializers.ModelSerializer):
    uid = serializers.IntegerField()
    sid = serializers.IntegerField()
    cid = serializers.IntegerField()
    content = serializers.CharField()

    class Meta:
        model = Comment
        fields = get_model_fields(Comment)
