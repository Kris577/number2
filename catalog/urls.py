from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('register/', views.register, name='register'),
    path('my_requests/', views.my_requests, name='my_requests'),
    path('create_request/', views.create_request, name='create_request'),
    path('request/<int:pk>/delete/', views.RequestDelete.as_view(), name='request_delete'),

    # --- URL-ы для администратора ---
    path('request/<int:pk>/change_status/', views.change_status, name='change_status'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),
]