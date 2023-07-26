from django.shortcuts import render
from .models import Movie
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import MovieSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class MovieListView(ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsOwnerOrReadOnly]