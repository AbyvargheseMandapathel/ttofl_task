from django.urls import path
from .views import LoginAPIView, SignUpAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('signup/', SignUpAPIView.as_view(), name='signup'),
]
