from django.db import models


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=64)
    checkPassword = models.CharField(max_length=64)

    def __str__(self):
        return self.firstName
