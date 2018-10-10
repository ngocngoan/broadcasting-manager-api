from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from broadcasts.models import Broadcast
from unit_prices.models import UnitPrice

# Create your models here.
CONTRACT_TYPES = (('Khai Thác', 'Khai Thác'), ('Tiếp Phát', 'Tiếp Phát'))
TAX = ((5, 5), (10, 10), (5.0, 5.0), (10.0, 10.0), (5.00, 5.00), (10.00, 10.00))


class Contract(models.Model):
    contract_number = models.CharField(max_length=20, blank=False, null=False)
    sign_date = models.DateField(blank=False, null=False)
    contract_type = models.CharField(max_length=10, choices=CONTRACT_TYPES, default=CONTRACT_TYPES[0][0])
    tax = models.FloatField(choices=TAX, default=TAX[1][0], validators=[MinValueValidator(0.00), MaxValueValidator(100.00)])
    cancel_date = models.DateField(blank=True, null=True)

    broadcast = models.OneToOneField(Broadcast, on_delete=models.SET_NULL, null=True)
    unit_price = models.ForeignKey(UnitPrice, on_delete=models.CASCADE)

    class Meta:
        db_table = "contracts"
