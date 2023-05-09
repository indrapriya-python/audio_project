from rest_framework import generics
from .models import Song
from .serializer import Songserializer
# Create your views here.

class Songcreate(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = Songserializer

class SongUpdate(generics.UpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = Songserializer

class SongDelete(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = Songserializer

