from django.db import models

from service.models import Services
from user.models import UserInfo
from utils.base_model import BaseModel



class Comment(BaseModel):
    uid = models.IntegerField(verbose_name='用户id', null=True)
    sid = models.IntegerField(verbose_name='服务id', null=True)
    cid = models.IntegerField(verbose_name='评论id', null=True)
    content = models.TextField(verbose_name='评论内容', null=True)
    class Meta:
        db_table = 'comment'
        verbose_name = '评论表'
        verbose_name_plural = verbose_name

    @property
    def user(self):
        '''当前评论的作者'''
        if not hasattr(self, '_user'):
            self._user = UserInfo.objects.get(self.uid)
        return self._user

    @property
    def service(self):
        '''当前评论的服务'''
        if not hasattr(self, '_service'):
            self._service = Services.objects.get(self.sid)
        return self._service

    @property
    def com(self):
        '''回复的评论'''
        if self.cid == 0:
            return None
        elif not hasattr(self, '_com'):
            self._com = Comment.objects.get(self.cid)
        return self._com



