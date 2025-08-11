from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('register', views.UserRegistrationView.as_view(), name='register'),
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),
    path('notes', views.NoteListView.as_view(), name='note-list'),
    path('notes/create', views.NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>', views.NoteDetailView.as_view(), name='note-detail'),
    path('notes/<int:pk>/delete', views.NoteDeleteView.as_view(), name='note-delete'),
    path('notes/<int:pk>/toggle', views.toggleNode, name='note-toggle'),
]