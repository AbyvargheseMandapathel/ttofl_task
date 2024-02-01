from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as auth_login
from .serializers import LoginSerializer, SignUpSerializer

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        auth_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'id': user.id, 'token': token.key}, status=status.HTTP_200_OK)

class SignUpAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if not user.is_superuser:
                user.generate_author_id()

            token, _ = Token.objects.get_or_create(user=user)
            return Response({'id': user.id, 'token': token.key}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
