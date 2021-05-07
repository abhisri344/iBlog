from django.urls import path
from . import views
urlpatterns = [
    # path('', views.index),
    path('blogs/', views.blogs),
    path('blogpost/<int:id>', views.blogpost),
    path('', views.home),
    path('add/',views.AddBlog.as_view()),
    path('search/',views.search),
    
]