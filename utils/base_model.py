from datetime import datetime

from django.db import models
from django.db.models import QuerySet, Q


class SoftDeletableQuerySet(QuerySet):
    def delete(self):
        self.update(is_deleted=True)


class SoftDeletableManager(models.Manager):
    _queryset_class = SoftDeletableQuerySet

    def get_queryset(self):
        """
        在这里处理一下QuerySet, 然后返回没被标记位is_deleted的QuerySet
        """
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints

        return self._queryset_class(**kwargs).filter(Q(is_deleted=False) | Q(is_deleted=None))
class BaseModel(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')
    create_user = models.CharField(max_length=50, null=True, verbose_name='创建用户名称')
    create_user_id = models.IntegerField(null=True, verbose_name='创建用户ID')

    last_modifier_time = models.DateTimeField(auto_now=True, null=True, verbose_name='上次修改时间')
    last_modifier_user = models.CharField(max_length=50, null=True, verbose_name='上次修改用户名称')
    last_modifier_user_id = models.IntegerField(null=True, verbose_name='上次修改用户ID')

    last_approval_time = models.DateTimeField(null=True, verbose_name='上次审阅时间')
    last_approval_user = models.CharField(max_length=50, null=True, verbose_name='上次审阅用户名称')
    last_approval_user_id = models.IntegerField(null=True, verbose_name='上次审阅用户ID')

    delete_time = models.DateTimeField(null=True, verbose_name='删除时间')
    delete_user = models.CharField(max_length=50, null=True, verbose_name='删除用户名称')
    delete_user_id = models.IntegerField(null=True, verbose_name='删除用户ID')

    # isapproval_success=models.BooleanField(default=False)

    is_deleted = models.BooleanField(null=True, verbose_name='假删')
    remark = models.CharField(max_length=500, null=True, verbose_name='备注')
    objects = SoftDeletableManager()

    def delete(self, using=None, soft=True, *args, **kwargs):

        if soft:
            from utils.custom_token import _thread_locals as tl
            cuser = getattr(tl, 'user', None)
            if cuser:
                self.delete_user = cuser.username
                self.delete_user_id = cuser.id
            self.is_deleted = True
            self.delete_time = datetime.now()
            self.save(using=using)
        else:
            return super(BaseModel, self).delete(using=using, *args, **kwargs)

    def save(self, *args, **kwargs):

        from utils.custom_token import _thread_locals as tl
        cuser = getattr(tl, 'user', None)

        if not self.id:
            self.creation_time = datetime.today()
            if cuser:
                self.create_user_id = cuser.id
                self.create_user = cuser.username
        self.last_modifier_time = datetime.today()
        if cuser:
            self.last_modifier_user = cuser.username
            self.last_modifier_user_id = cuser.id
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
