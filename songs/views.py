from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer

@api_view(['GET', 'POST'])
def songs_list(request):

    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

@api_view(['GET', 'PUT'])
def song_detail(request, pk):
    if request.method == 'GET':
        song = get_object_or_404(Song, pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        song = get_object_or_404(Song, pk=pk)
        serializer = SongSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



