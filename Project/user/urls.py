from django.urls import path
from . import views
urlpatterns = [
      path('dashboard/', views.dashboard, name='dashboard'),
      path('dashboard2/', views.dashboard, name='dashboard2'),
      path('login/', views.user_login, name='login'),
      path('register/', views.register, name='register'),
]
