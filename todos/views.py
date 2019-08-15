from django.http import HttpResponse
from .models import Category, Todo
from .serializers import CategorySerializer, TodoSerializer
from rest_framework import generics


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!!")


class ListCreateCategories(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RetrieveUpdateDestroyCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListCreateTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class RetrieveUpdateDestroyTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
