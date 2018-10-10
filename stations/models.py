from django.db import models

from areas.models import Area
from televisions.models import Television

# Create your models here.
BY_CONTRACT = 'Hợp đồng'
BY_DIRECT = 'Trực tiếp'
MANAGE_TYPE = (
    (BY_CONTRACT, 'Hợp đồng'),
    (BY_DIRECT, 'Trực tiếp')
)


class Station(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    alias_name = models.CharField(max_length=50, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    location = models.CharField(max_length=100, blank=False, null=False)
    manage_type = models.CharField(max_length=10, choices=MANAGE_TYPE, default=BY_CONTRACT)
    description = models.TextField(blank=True, null=True)

    television = models.ForeignKey(Television, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "stations"
