
from django.db import models
from django.conf import settings

# Create your models here.





class Emails(models.Model):
    address = models.EmailField(verbose_name='email')
    def __str__(self):
        return self.address