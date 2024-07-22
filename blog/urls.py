from django.urls import path
from .views import PostListCreate, PostRetrieveUpdateDestroy, CommentListCreate,UserRegistrationView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroy.as_view(), name='post-detail'),
    path('posts/<int:post_pk>/comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('signup/', UserRegistrationView.as_view(), name='user-signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

