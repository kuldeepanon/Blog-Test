from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserSignupView
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:pk>/like/', PostViewSet.as_view({'post': 'like_post'}), name='like-post'),
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]