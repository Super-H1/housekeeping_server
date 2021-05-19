from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from comment.models import Comment
from comment.serializers import CommentSerializer


class CommentViewset(ModelViewSet):
    queryset = Comment.objects.all().order_by('-creation_time')
    serializer_class = CommentSerializer
    lookup_field = 'pk'


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



