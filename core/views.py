from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from author.serializers import AuthorSerializer
from books.models import Genre, Book
from author.models import Author
from books.serializers import BookSerializer, GenreSerializer
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404


class GenreAPIView(APIView):
    permission_classes = [IsAdminUser]


    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            genre = serializer.save()
            print(f"Genre '{genre.name}' saved successfully.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GenreDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]

    
    def delete(self, request, pk):
        try:
            genre = Genre.objects.get(pk=pk)
            genre.delete()
            return Response({'Success': 'Genre deleted.'},status=status.HTTP_204_NO_CONTENT)
        except Genre.DoesNotExist:
            return Response({'error': 'Genre not found.'}, status=status.HTTP_404_NOT_FOUND)
    
class AuthorListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]


    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser]
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BookSerializer

    def get_queryset(self):
        author_id = self.kwargs.get('pk')
        author = get_object_or_404(Author, id=author_id)
        return Book.objects.filter(author=author)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Author.DoesNotExist:
            return Response({'error': 'Author not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


