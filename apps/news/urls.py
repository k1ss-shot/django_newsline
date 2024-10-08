from django.urls import path
from . import views

from apps.news.views import PostListView, PostDetailView

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
]

