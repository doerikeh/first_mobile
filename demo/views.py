from .seriallizer import BookSerializers
from .models import Book

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BookViewSets(viewsets.ModelViewSet):
    serializer_class = BookSerializers
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)