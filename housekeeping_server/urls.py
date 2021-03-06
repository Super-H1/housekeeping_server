"""HouseKeeping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^api/basic/', include('basic.urls')),
    url('^api/auth/', include('Auth.urls')),
    url('^api/user/', include('user.urls')),
    url('^api/category/', include('category.urls')),
    url('^api/service/', include('service.urls')),
    url(r'^api/remark/', include('comment.urls')),
    url(r'^api/cart/', include('cart.urls')),
    url(r'^api/address/', include('address.urls')),
    url(r'^api/order/', include('order.urls')),
    url(r'^api/reward/', include('reward.urls')),
    url(r'^api/collect/', include('collect.urls')),
    url(r'^api/comment/', include('comment.urls'))
]
