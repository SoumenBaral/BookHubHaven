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
    Content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='bookCollection/media/uploads/', blank = True, null = True)

    def __str__ (self):
        return self.Name

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userReview')
    post = models.ForeignKey(AddBook, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"
