from django.urls import path
from .display import views

app_name = 'speaker_management'

urlpatterns = [
    path('', views.SpeakerListView.as_view(), name='list'),
    path('<int:pk>/', views.SpeakerDetailView.as_view(), name='detail'),
    path('create/', views.SpeakerCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.SpeakerUpdateView.as_view(), name='update'),
    # Delete URL removed - not in structure chart
]