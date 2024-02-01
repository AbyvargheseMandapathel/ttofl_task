from django.db import models
from author.models import Author

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    name = models.CharField( max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    pages = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='books/', null=True, blank=True)

    def __str__(self):
        return self.name
