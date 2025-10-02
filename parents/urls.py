from django.urls import path
from . import views


urlpatterns = [
  path('parents/', views.parents_view, name='parents'),
  path('parents/create/', views.parent_create, name="parent_create"),
]