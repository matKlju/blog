from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostSearchView, PostRetrieveAPIView, PostListAPIView
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('blog/', PostListView.as_view(), name='post_list'),
    path('posts/', PostListView.as_view(), name='post_list'),

    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    path('new/', PostCreateView.as_view(), name='post_create'),
    path('blog/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),

    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('blog/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),

    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('search/', PostSearchView.as_view(), name='post_search'),

    path('api/posts/', PostListAPIView.as_view(), name='post_list_api'),
    path('api/posts/<int:pk>/', PostRetrieveAPIView.as_view(), name='post_detail_api'),

]
