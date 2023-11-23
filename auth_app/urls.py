from django.urls import path
from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.logout, name='logout'),
]