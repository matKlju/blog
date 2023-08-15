from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/new/', views.PostCreate.as_view()),
    path('posts/<int:pk>/edit/', views.PostUpdate.as_view()),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view()),
]
