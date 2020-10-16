from django.utils import timezone
from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    SKU = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()
    product_category = models.CharField(max_length=100)
    product_stock = models.IntegerField(blank=False, null=False)
    product_location = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    product_updated = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.product_updated = timezone.now()
        self.save()

