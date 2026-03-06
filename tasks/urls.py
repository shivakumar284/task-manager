from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('delete/<int:id>/',views.delete_task,name='delete_task'),
    path('toggle_complete/<int:id>/', views.toggle_complete, name='toggle_complete'),
    path('edit/<int:id>/',views.edit_task,name='edit_task'),
]