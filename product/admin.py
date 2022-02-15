from distutils.command.register import register
import imp
from django.contrib import admin

# Register your models here.

from .models import Product , Image , Category , Accessories , Alterative


admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Alterative)
admin.site.register(Accessories)