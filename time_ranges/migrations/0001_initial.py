# Generated by Django 2.0.1 on 2018-01-24 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('broadcasting_status', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(choices=[(1, 'Khung giờ phát sóng'), (2, 'mất sóng do sự cố máy phát'), (3, 'mất sóng máy phát do nguyên nhân khác'), (4, 'mất sóng tín hiệu')], default=1)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('broadcasting_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_range', to='broadcasting_status.BroadcastingStatus')),
            ],
            options={
                'db_table': 'time_ranges',
            },
        ),
    ]
