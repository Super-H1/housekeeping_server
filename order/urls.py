from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from order import views

router = DefaultRouter()
router.register('make_order', views.OrderViewset, basename='make_order')
router.register('show_order', views.OrderViewset, basename='show_order')
router.register('get_list', views.OrderViewset, basename='get_list')
router.register('del_order', views.OrderViewset, basename='del_order')
urlpatterns = [
    url(r'^pay_order/$', views.OrderViewset.as_view({'post': 'pay_order'})),
    url(r'^confirm_pay/$', views.OrderViewset.as_view({'post': 'confirm_pay'})),
    url(r'^servicer_accept_order/$', views.OrderViewset.as_view({'post': 'servicer_accept_order'})),
    url(r'^servicer_refuse_order/$', views.OrderViewset.as_view({'post': 'servicer_refuse_order'})),
    url(r'^servicer_complete_order/$', views.OrderViewset.as_view({'post': 'servicer_complete_order'})),
    url(r'^user_confirm_complete_order/$', views.OrderViewset.as_view({'post': 'user_confirm_complete_order'})),
    url(r'^user_refund/$', views.OrderViewset.as_view({'post': 'user_refund'})),
    url(r'^admin_agree_refund/$', views.OrderViewset.as_view({'post': 'admin_agree_refund'})),
    url(r'^admin_agree_complain/$', views.OrderViewset.as_view({'post': 'admin_agree_complain'})),

]

urlpatterns += router.urls
