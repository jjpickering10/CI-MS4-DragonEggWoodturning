import uuid
from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(max_length=254, default='Sorry, no description currently')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    on_sale = models.BooleanField(default=False)
    on_sale_amount = models.IntegerField(null=True, blank=True)

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
    DISCOUNT_OPTIONS = (
        (5, '5% off'),
        (10, '10% off'),
        (15, '15% off'),
        (25, '25% off'),
        (50, '50% off'),
    )
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    wood_type = models.ManyToManyField(WoodType)
    sku = models.CharField(max_length=254, default='sku', blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discounted = models.BooleanField(default=False)
    discount_choices = models.IntegerField(choices=DISCOUNT_OPTIONS, null=True, blank=True)
    final_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

    def _generate_sku(self):
        """
        Generate a random, unique sku using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_rating(self):
        self.rating = self.review_set.aggregate(Avg('rating'))['rating__avg'] or 0
        self.save()

    def add_discount(self):
        if self.discount_choices:
            self.discounted = True
        else:
            self.discounted = False

    def generate_final_price(self):
        if self.discounted:
            # print(self.discount_choices)
            # print(self.price)
            discount_amount = (self.price / 100) * self.discount_choices
            # print(discount_amount)
            final_amount = self.price - discount_amount
            # print(final_amount)
            self.final_price = round(final_amount, 2)
        else:
            self.final_price = self.price

    def check_category_on_sale(self):
        if self.category.on_sale:
            self.discount_choices = self.category.on_sale_amount
            print(self.discount_choices)
            self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the sku
        if it hasn't been set already
        """
        if self.sku == 'sku':
            self.sku = self._generate_sku()
        self.add_discount()
        self.generate_final_price()
        super().save(*args, **kwargs)


class Image(models.Model):

    class Meta:
        verbose_name_plural = 'Images'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product.name


class Review(models.Model):

    RATINGS_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    body = models.TextField()
    rating = models.IntegerField(choices=RATINGS_CHOICES, default=0)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product.name
