from .serializers import TodoSerializer
from .models import Todo
from rest_framework import generics


class ListAsView(generics.ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class DetailAsView(generics.RetrieveAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()



