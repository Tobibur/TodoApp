from django.urls import path

from . import views
from .views import ListCategories, ListTodo

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', ListCategories.as_view(), name="categories-all"),
    path('todo/', ListTodo.as_view(), name="todo-all")
]
