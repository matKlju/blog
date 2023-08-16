from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList),
    path('posts/<int:pk>/', views.PostDetail),
    path('posts/new/', views.PostCreate),
    path('posts/<int:pk>/edit/', views.PostUpdate),
    path('posts/<int:pk>/delete/', views.PostDelete),
]
