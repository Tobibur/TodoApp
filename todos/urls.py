from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^categories/$', views.ListCreateCategories.as_view(), name="categories-all"),
    url(r'^categories/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyCategory.as_view(), name="category_detail"),
    url(r'^todo/$', views.ListCreateTodo.as_view(), name="todo-all"),
    url(r'^todo/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyTodo.as_view(), name="todo_detail"),
]
