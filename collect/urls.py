from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from collect import views
router = DefaultRouter()
router.register('add_collect', views.CollectViewset, basename='add_collect')
router.register('get_collect', views.CollectViewset, basename='add_collect')
router.register('collect_list', views.CollectViewset, basename='collect_list')

urlpatterns = [
    url(r'change_status/', views.CollectViewset.as_view({'post': 'change_status'}))
]

urlpatterns += router.urls

