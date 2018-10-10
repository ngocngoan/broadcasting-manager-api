from django.db import models

from broadcasting_status.models import BroadcastingStatus
from django.db.models import DurationField, ExpressionWrapper, F

# Create your models here.
TYPES = (
    (1, 'Khung giờ phát sóng'),
    (2, 'mất sóng do sự cố máy phát'),
    (3, 'mất sóng máy phát do nguyên nhân khác'),
    (4, 'mất sóng tín hiệu'),
)


class TimeRange(models.Model):
    type = models.SmallIntegerField(choices=TYPES, default=TYPES[0][0])
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)

    broadcasting_status = models.ForeignKey(BroadcastingStatus, on_delete=models.CASCADE, related_name='time_range')

    # @property
    # def get_duration(self):
    #     return ExpressionWrapper(F(self.end_time) - F(self.start_time), output_field=DurationField())

    class Meta:
        db_table = "time_ranges"
