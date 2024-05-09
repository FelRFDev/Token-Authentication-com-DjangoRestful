from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    adress = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)


    def __str__(self):
        return '{self.name} - [{self.email}]'
    

    class Meta:
        verbose_name= 'Registration forms'
