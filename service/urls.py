from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from service import views

router = DefaultRouter()
router.register(r'addservice', viewset=views.ServiceViewset, basename='addservice')
router.register(r'services', viewset=views.ServiceViewset, basename='services')
urlpatterns = [
    url(r'^servieces/(?P<pk>[0-9]+)/$', views.ServiceViewset.as_view({'get': 'list'}))
]
urlpatterns += router.urls
print(router.urls)
