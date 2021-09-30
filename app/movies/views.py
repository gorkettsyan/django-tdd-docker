from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ViewSet):
    queryset = Movie.objects.all()
    def create(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def retrieve(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = MovieSerializer(queryset)

        return Response(serializer.data)