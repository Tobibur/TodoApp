from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Todo
from .serializers import CategorySerializer, TodoSerializer
from rest_framework import generics


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!!")


class ListCategories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
