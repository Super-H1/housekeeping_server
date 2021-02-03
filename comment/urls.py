from rest_framework.routers import DefaultRouter
from comment import views

router = DefaultRouter()
router.register(r'send_comment', viewset=views.CommentViewset, basename='send_comment')
router.register(r'comments', viewset=views.CommentViewset, basename='comments')

urlpatterns = [

]

urlpatterns += router.urls

