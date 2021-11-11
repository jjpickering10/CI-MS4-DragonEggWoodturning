import uuid
from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(max_length=254, default='Sorry, no description currently')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class WoodType(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    wood_type = models.ManyToManyField(WoodType)
    sku = models.CharField(max_length=254, default='sku', blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

    def _generate_sku(self):
        """
        Generate a random, unique sku using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the sku
        if it hasn't been set already
        """
        if self.sku == 'sku':
            self.sku = self._generate_sku()
        super().save(*args, **kwargs)


class Image(models.Model):

    class Meta:
        verbose_name_plural = 'Images'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product.name
