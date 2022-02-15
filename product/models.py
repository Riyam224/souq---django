
import imp
import re
from xmlrpc.client import boolean
from django.db import models
from django.forms import BooleanField
from django.utils.translation import gettext as _
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Product(models.Model):
    name = models.CharField(_("name"), max_length=50)
    desc = models.TextField(_("desc"))
    category = models.ForeignKey("Category", verbose_name=_("category"), on_delete=models.CASCADE , blank=True, null=True)
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2)
    Discountprice = models.DecimalField(_("Discountprice"), max_digits=5, decimal_places=2)
    cost =models.DecimalField(_("cost"), max_digits=5, decimal_places=2)
    product_image = models.ImageField(_("image"), upload_to='product/', blank=True, null=True)
    brand = models.ForeignKey("settings.Brand", verbose_name=_("brand"), on_delete=models.CASCADE, blank=True, null=True)
    variant = models.ForeignKey("settings.Variant", verbose_name=_("variant"), on_delete=models.CASCADE, blank=True, null=True)
    
    isNew = models.BooleanField(_("is new") , default=True)
    isBestSeller = models.BooleanField(_("is best seller") , default=False)

    created = models.DateTimeField(_("created"),auto_now_add=True)
    updated = models.DateTimeField(_("updated"), auto_now=True)

    slug = models.SlugField(_("slug") , blank=True, null=True)
   
    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("product:product_detail", kwargs={"slug": self.slug})
    

    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Product , self).save( *args, **kwargs)



class Image(models.Model):
    """Model definition for Image."""

    product = models.ForeignKey(Product, verbose_name=_("image"), on_delete=models.CASCADE)
    image = models.ImageField(_("image "), upload_to='images/' , blank=True, null=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Image."""

        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        """Unicode representation of Image."""
        return str(self.product.name)




class Category(models.Model):
    name = models.CharField(_("name"), max_length=50)
    category_parent = models.ForeignKey("self", limit_choices_to={'category_parent__isnull' :True} ,  verbose_name=_("category parent"), on_delete=models.CASCADE, blank=True, null=True)
    desc = models.TextField(_("description"))
    image = models.ImageField(_("image"), upload_to='category/', blank=True, null=True)


    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name




class Alterative(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("product"), related_name='main_product', on_delete=models.CASCADE)
    alternatives  = models.ManyToManyField(Product, related_name='alterative_products', verbose_name=_("alternatives"))

    class Meta:
        verbose_name = _("Alterative")
        verbose_name_plural = _("Alteratives")

    def __str__(self):
        return str(self.product)


class Accessories(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("product "), related_name='product_main', on_delete=models.CASCADE)
    accessories  =  models.ManyToManyField(Product, related_name='product_accessories', verbose_name=_("accesspries"))
    

    class Meta:
        verbose_name = _("Accessories")
        verbose_name_plural = _("Accessoriess")

    def __str__(self):
        return str(self.product)

