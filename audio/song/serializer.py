from rest_framework import serializers
from .models import Song

class Songserializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'