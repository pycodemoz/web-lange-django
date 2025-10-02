from django.urls import path
from . import views


urlpatterns = [
  path('users/', views.registration_view, name='users'),
]