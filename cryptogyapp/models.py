from django.db import models

# Create your models here.
class Cryptosystem(models.Model):
    icon = models.ImageField(default='/staticfiles/assets/default.jpg')
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1200)

    def __str__(self):
        return self.name

class RSAInput(models.Model):
    primeP = models.CharField(max_length=4294967296, blank=True)
    primeQ = models.CharField(max_length=4294967296, blank=True)
    clearText = models.CharField(max_length=4294967296, blank=True)    
    cipherText = models.CharField(max_length=4294967296, blank=True)

class RSADSSInput(models.Model):
    primeP = models.CharField(max_length=4294967296, blank=True)
    primeQ = models.CharField(max_length=4294967296, blank=True)
    message = models.CharField(max_length=4294967296, blank=True)
    clearFile = models.FileField(blank = True) 
    signature = models.CharField(max_length=4294967296, blank=True)

class RabinInput(models.Model):
    primeP = models.CharField(max_length=4294967296, blank=True)
    primeQ = models.CharField(max_length=4294967296, blank=True)
    clearText = models.CharField(max_length=4294967296, blank=True)    
    cipherText = models.CharField(max_length=4294967296, blank=True)

class MVInput(models.Model):
    pubKey = models.CharField(max_length=4294967296, blank=True, default='-')
    privKey = models.CharField(max_length=4294967296, blank=True, default='-')
    clearText = models.CharField(max_length=4294967296, blank=True)
    cipherText = models.CharField(max_length=4294967296, blank=True)

class GammalInput(models.Model):
    pubKey = models.CharField(max_length=4294967296, blank=True, default='-')
    privKey = models.CharField(max_length=4294967296, blank=True, default='-')
    clearText = models.CharField(max_length=4294967296, blank=True)
    cipherText = models.CharField(max_length=4294967296, blank=True)

class GammalDSSInput(models.Model):
    pubKey = models.CharField(max_length=4294967296, blank=True, default='-')
    privKey = models.CharField(max_length=4294967296, blank=True, default='-')
    message = models.CharField(max_length=4294967296, blank=True)
    clearFile = models.FileField(blank = True)
    signature = models.CharField(max_length=4294967296, blank=True)

class ImageEncryptionInput(models.Model):
    clearImage = models.ImageField(upload_to='images', blank = True)
    cipherImageT1 = models.ImageField(upload_to='images', blank = True)
    cipherImageT2 = models.ImageField(upload_to='images', blank = True)