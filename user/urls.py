from django.conf.urls import url

from user.views import UserView

urlpatterns = [
    url(r'^update/(?P<pk>[0-9]+)/', UserView.as_view())
]
