from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.get_posts, name='get_posts'),
    path('posts/<int:id>/', views.get_post, name='get_post'),
]
