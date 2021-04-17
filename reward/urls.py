from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from reward import views

router = DefaultRouter()
router.register(r'reward_list', viewset=views.RewardViewset, basename='reward_list')
urlpatterns = [
    url(r'^release_reward/$', views.RewardViewset.as_view({'post': 'release_reward'})),
]
urlpatterns += router.urls
print(router.urls)
