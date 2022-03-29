from django.db import models

# Create your models here.
class Cryptosystem(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1200)

    def __str__(self):
        return self.name