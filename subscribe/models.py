from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Emails(models.Model):
    address = models.EmailField()
    def __str__(self):
        return self.address