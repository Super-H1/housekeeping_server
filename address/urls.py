from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from address import views

router = DefaultRouter()
router.register(r'addaddress', views.AddressViewset, basename='addaddress')
router.register(r'list', views.AddressViewset, basename='address_list')
router.register(r'deladdress', views.AddressViewset, basename='del_address')
router.register(r'addressdetail', views.AddressViewset, basename='address_detail')
router.register(r'address', views.AddressViewset, basename='address')

urlpatterns = [
    url(r'^set_default_address/', views.AddressViewset.as_view({'post': 'set_default_address'})),
    url(r'^get_default_address/', views.AddressViewset.as_view({'get': 'get_default_address'})),
]
urlpatterns += router.urls
print(router.urls)
