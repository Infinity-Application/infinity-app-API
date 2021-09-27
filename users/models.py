from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
       return self.email


