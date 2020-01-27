from django.contrib import admin
from .models import Book, BookNumber, Character

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'id', 'harga', 'descrioption']
    list_display = ['title', 'descrioption']
    list_filter = ['publish']

admin.site.register(BookNumber)
admin.site.register(Character)