from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
class Activities(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Posts(models.Model):
    file = models.FileField(upload_to='posts/')
    description = models.TextField()

    def __str__(self):
        return self.description
    