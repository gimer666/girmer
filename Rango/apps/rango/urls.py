from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'rango'

urlpatterns = [
    path('', views.index , name='index'),
    path('about/', views.about, name='about'),
    path('category/slug:category_name_slug/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('restricted/', views.restricted, name='restricted')
]