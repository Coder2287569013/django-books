from django.db import models

# Create your models here.
class LibraryBook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Library"
        ordering = ["author"]