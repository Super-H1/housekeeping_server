from rest_framework.routers import DefaultRouter

from cart import views

router = DefaultRouter()
router.register('add_to_cart', views.CartViewSet, basename='addTocart')
router.register('lists', views.CartViewSet, basename='cart_list')
router.register('carts', views.CartViewSet, basename='carts')
urlpatterns = [
]
urlpatterns += router.urls