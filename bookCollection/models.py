from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    Name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return self.Name



class AddBook(models.Model):
    Name  = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0 , default=0.00)
    quantity = models.IntegerField(default=0)
    Content = models.TextField()
    brand = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='bookCollection/media/uploads/', blank = True, null = True)

    def __str__ (self):
        return self.Name
