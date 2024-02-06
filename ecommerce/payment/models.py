from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ShippingAddress(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Shipping Address"

    def __str__(self):
        return 'Shipping Address - ' + str(self.id)