from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from order import views

router = DefaultRouter()
router.register('make_order', views.OrderViewset, basename='make_order')
router.register('show_order', views.OrderViewset, basename='show_order')
router.register('get_list', views.OrderViewset, basename='get_list')
router.register('del_order', views.OrderViewset, basename='del_order')
urlpatterns = [
    url(r'^pay_order/$', views.OrderViewset.as_view({'post': 'pay_order'}))
]

urlpatterns += router.urls
