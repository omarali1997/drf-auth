from django.shortcuts import render
from .models import Snack
from .permissions import IsOwnerOrReadOnly

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SweetSerializer


class SnackListView(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SweetSerializer

class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SweetSerializer
    Permission_classes=[IsOwnerOrReadOnly]


