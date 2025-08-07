from django.urls import path
from .display import views

app_name = 'member_management'

urlpatterns = [
    path('', views.MemberListView.as_view(), name='list'),
    path('<int:pk>/', views.MemberDetailView.as_view(), name='detail'),
    path('create/', views.MemberCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.MemberUpdateView.as_view(), name='update'),
    # Delete URL removed - not in structure chart
]