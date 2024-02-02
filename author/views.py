from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as auth_login

from books.models import Book
from .serializers import LoginSerializer, SignUpSerializer
from books.serializers import BookSerializer
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404


class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        auth_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'id': user.id, 'token': token.key}, status=status.HTTP_200_OK)

class SignUpAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if not user.is_superuser:
                user.generate_author_id()

            token, _ = Token.objects.get_or_create(user=user)
            return Response({'id': user.id, 'token': token.key}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


class AddBookAPIView(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class EditBookAPIView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        author_books = self.request.user.books.all()  
        return author_books

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        return get_object_or_404(queryset, pk=pk)
