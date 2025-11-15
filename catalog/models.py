from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomerUser(AbstractUser):
     full_name = models.CharField(max_length=150)
     email = models.EmailField(unique=True)

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="name category")
    def __str__(self):
        return self.name

class RequestDesing(models.Model):
    STATUS_CHOICES = (
        ('n', 'new'),
        ('h', 'hired'),
        ('с', 'completed')
    )

    title = models.CharField(max_length=200, verbose_name="title")
    description = models.TextField(verbose_name="description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="category")
    date = models.DateTimeField(auto_now_add=True, verbose_name="creation date")
    image = models.ImageField(default='default.jpg', upload_to="images/", verbose_name="image")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='n', verbose_name="status")
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, null=True, verbose_name="customer")