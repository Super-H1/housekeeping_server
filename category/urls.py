from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from category import views

router = DefaultRouter()
router.register(r'addcategory', views.CategoryViewset, basename='addcategory')
router.register(r'categorys', views.CategoryViewset, basename='categorys')

urlpatterns = [
    # url(r'^addcategory/$', views.CategoryViewset.as_view()),
    # url(r'^list/$', views.CategoryViewset.as_view())
]

urlpatterns += router.urls

