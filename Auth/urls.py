from django.conf.urls import url

from Auth import views

urlpatterns = [
    url(r'^login/', views.LoginView.as_view()),
]
