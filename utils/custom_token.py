# encoding=utf-8
from rest_framework_simplejwt.tokens import AccessToken
from threading import local

_thread_locals = local()


def set_current_user(user):
    _thread_locals.user = user


def get_current_user():
    return getattr(_thread_locals, 'user', None)

#暂未使用到
class CurrentUserMiddleware(object):
    def process_request(self, request):
        set_current_user(getattr(request, 'user', None))

def usertoken_md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()


def get_token(request):
    str_token = request.headers['Authorization']
    str_token = str_token.replace('Bearer ', '')
    token = AccessToken(str_token)
    return token



