from rest_framework import serializers
from .models import Book, BookNumber

class BookNumberSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_30']

class BookSerializers(serializers.ModelSerializer):
    isbn = BookNumberSerializers(many=False)

    class Meta:
        model = Book
        fields = ['id', 'title', 'harga', 'publish', 'descrioption', 'isbn']