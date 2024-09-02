from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_count = models.IntegerField()
    category = models.CharField(max_length=100)
    sales_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def popularity(self):
        return self.sales_count / max(self.inventory_count, 1)