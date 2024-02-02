from django.urls import path
from .views import AuthorListAPIView, BookListAPIView, ExportBooksAPIView, GenreAPIView, GenreDeleteAPIView,AuthorDetailAPIView

urlpatterns = [
    path('create/', GenreAPIView.as_view(), name='genre-create'),
    path('<int:pk>/', GenreDeleteAPIView.as_view(), name='genre-delete'),
    path('', AuthorListAPIView.as_view(), name='author-list'),
    path('<str:pk>/', AuthorDetailAPIView.as_view(), name='author-detail'),
    path('<str:pk>/books/', BookListAPIView.as_view(), name='author-books'),
    # path('<int:pk>/export-books/', ExportBooksAPIView.as_view(), name='export_books'),
    path('export-books/<int:pk>/', ExportBooksAPIView.as_view(), name='export-books'),
]
