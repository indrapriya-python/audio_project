from .views import *
from django.urls import path

urlpatterns = [
    
    path('',Songcreate.as_view()),
    path('create/',SongUpdate.as_view()),
    path('delete/<int:pk>',SongDelete.as_view()),


]
