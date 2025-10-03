from django.urls import path
from . import views


urlpatterns = [
  path('parents/', views.parents_view, name='parents'),
  path('parents/create/', views.parent_create, name="parent_create"),
  path('parents/<int:pk>/update/', views.parent_update, name='parent_update'),
  path('parents/<int:pk>/delete/', views.parent_delete, name='parent_delete'),
]