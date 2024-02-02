from rest_framework import serializers
from .models import Genre , Book

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','name', 'pages', 'author', 'genre', 'cover_image']
        
        read_only_fields = ['author'] 
    def validate_author(self, value):
        
        if self.instance is None:
            return self.context['request'].user
        return value