from django.urls import path
from .views import LoginAPIView, SignUpAPIView,AddBookAPIView,EditBookAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('add-book/', AddBookAPIView.as_view(), name='add_book'),
    path('edit-book/<int:pk>/', EditBookAPIView.as_view(), name='edit_book'),
]
