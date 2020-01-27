from django.db import models



class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=30, blank=True)
    isbn_30 = models.CharField(max_length=30, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False, null=True, unique=True)
    descrioption = models.TextField(blank=True)
    harga = models.DecimalField(default=0, max_digits=12, decimal_places=3)
    publish = models.DateField(blank=True, default=None, null=True)
    is_publish = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)

    isbn = models.OneToOneField(BookNumber, on_delete=models.CASCADE, null=True, blank=False)
    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=50)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

