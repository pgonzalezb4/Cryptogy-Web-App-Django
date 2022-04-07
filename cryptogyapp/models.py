from django.db import models

# Create your models here.
class Cryptosystem(models.Model):
    icon = models.ImageField(upload_to = 'media/', default='/staticfiles/assets/default.jpg')
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1200)

    def __str__(self):
        return self.name

class RSAInput(models.Model):
    primeP = models.BigIntegerField(blank=True)
    primeQ = models.BigIntegerField(blank=True)
    clearText = models.CharField(max_length=1200, blank=True)    
    cipherText = models.CharField(max_length=1200, blank=True)