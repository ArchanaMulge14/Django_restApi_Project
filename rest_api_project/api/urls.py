from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView, ParagraphListCreateAPIView, ParagraphRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('paragraphs/', ParagraphListCreateAPIView.as_view(), name='paragraph-list'),
    path('paragraphs/<int:pk>/', ParagraphRetrieveUpdateDestroyAPIView.as_view(), name='paragraph-detail'),
]
