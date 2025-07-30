from django.urls import path
from .display import views

app_name = 'event_management'

urlpatterns = [
    path('', views.EventListView.as_view(), name='list'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='detail'),
    path('create/', views.EventCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.EventUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.EventDeleteView.as_view(), name='delete'),
    path('<int:pk>/register/', views.register_for_event, name='register'),
]