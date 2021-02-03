from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from basic import views

router = DefaultRouter()
router.register(r'upload', views.FileUploadViewset, basename='FileUpload')

urlpatterns = [
    url(r'getcredential/$', views.CredentialView.as_view())
]

urlpatterns += router.urls
print(router.urls)
