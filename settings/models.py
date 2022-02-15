from django.db import models
# Create your models here.
from django.utils.translation import gettext as _


class Brand(models.Model):
    name = models.CharField(_("name"), max_length=50)
    desc = models.TextField(_("desc"))
    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.name

class Variant(models.Model):
    name = models.CharField(_("name"), max_length=50)
    desc = models.TextField(_("desc") , blank=True, null=True)
    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        return self.name
