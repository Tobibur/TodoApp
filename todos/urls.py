from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.ListCreateCategories.as_view(), name="categories-all"),
    path('categories/<int:pk>/', views.RetrieveUpdateDestroyCategory.as_view(), name="category_detail"),
    path('todo/', views.ListCreateTodo.as_view(), name="todo-all"),
    path('todo/<int:pk>/', views.RetrieveUpdateDestroyTodo.as_view(), name="todo_detail"),
]
