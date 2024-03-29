from rest_framework import generics
from .models import CustomUser, Paragraph
from .serializers import UserSerializer, ParagraphSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class ParagraphListCreateAPIView(generics.ListCreateAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer

class ParagraphRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer

