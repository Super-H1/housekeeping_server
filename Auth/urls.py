from django.conf.urls import url

from Auth import views

urlpatterns = [
    url(r'^login/', views.LoginView.as_view()),
    url(r'^update_user/', views.LoginView.as_view()),
    url(r'^getcode/', views.CodeView.as_view()),

]
