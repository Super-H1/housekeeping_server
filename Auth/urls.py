from django.conf.urls import url


from Auth.views import LoginView, CodeView

urlpatterns = [
    url(r'login/$', LoginView.as_view()),
    url(r'getcode/$', CodeView.as_view()),

]
