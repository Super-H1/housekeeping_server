from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from comment.models import Comment
from comment.serializers import CommentSerializer


class CommentViewset(ModelViewSet):
    queryset = Comment.objects.all().order_by('-creation_time')
    serializer_class = CommentSerializer
    lookup_field = 'pk'



