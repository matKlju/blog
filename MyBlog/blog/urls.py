from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('blog/', PostListView.as_view(), name='post_list'),

    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),


    path('new/', PostCreateView.as_view(), name='post_create'),

    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),

    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
