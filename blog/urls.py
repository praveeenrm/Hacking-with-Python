from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:blog_id>', views.single_blog, name='single-blog'),
    path('about/', views.about, name='about'),
    path('resource/', views.resource, name='resource'),
    path('mailing/', views.mailing, name='mailing'),
]
