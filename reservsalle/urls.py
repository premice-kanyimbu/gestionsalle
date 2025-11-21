from django.contrib import admin
from django.urls import path
from reservsalle import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_views, name='index'),
    path('contact/', views.contact_views, name='contact'),
    path('articles/', views.articles_views, name='atricles'),
]
