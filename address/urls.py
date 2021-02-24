from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from address import views

router = DefaultRouter()
router.register(r'addaddress', views.AddressViewset, basename='addaddress')


urlpatterns = [
]

