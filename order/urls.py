from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from order import views

router = DefaultRouter()
router.register('make_order', views.OrderViewset, basename='make_order')
router.register('show_order', views.OrderViewset, basename='show_order')
urlpatterns = [

]

urlpatterns += router.urls
