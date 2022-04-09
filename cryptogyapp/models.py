from django.db import models

# Create your models here.
class Cryptosystem(models.Model):
    icon = models.ImageField(default='/staticfiles/assets/default.jpg')
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1200)

    def __str__(self):
        return self.name

class RSAInput(models.Model):
    primeP = models.DecimalField(max_digits=78, decimal_places=0)
    primeQ = models.DecimalField(max_digits=78, decimal_places=0)
    clearText = models.CharField(max_length=65536, blank=True)    
    cipherText = models.CharField(max_length=65536, blank=True)

class RabinInput(models.Model):
    primeP = models.DecimalField(max_digits=78, decimal_places=0)
    primeQ = models.DecimalField(max_digits=78, decimal_places=0)
    clearText = models.CharField(max_length=65536, blank=True)    
    cipherText = models.CharField(max_length=65536, blank=True)