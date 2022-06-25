from django.contrib import admin
from .models import Cryptosystem, Block

# Register your models here.
admin.site.register(Cryptosystem)
admin.site.register(Block)