from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'), # >> adds to the URL with /post and follows post with the post number i.e. 127.0.0.1:8000/post/1/ <<
    path('post/new/', views.post_new, name = 'post_new'),
    path('post/<int:pk>/edit/', views.edit_post, name = 'edit_post'),
]