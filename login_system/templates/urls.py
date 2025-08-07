from django.urls import path
from . import views

app_name = 'login_system'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('main-menu/', views.main_menu_view, name='main_menu'),
    path('logout/', views.logout_view, name='logout'),
]