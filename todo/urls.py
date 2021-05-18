from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('create/', views.create_todo, name = 'create-todo'),
    path('<id>/todo/', views.todo_detail, name = 'todo-detail'),
    path('<id>/todo-delete/', views.todo_delete, name = 'todo-delete'),
    path('<id>/todo-edit/', views.todo_edit, name = 'todo-edit'),
]
