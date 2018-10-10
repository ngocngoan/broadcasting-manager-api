# Generated by Django 2.0.1 on 2018-01-24 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('machine_locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broadcasting_hours', models.CharField(choices=[('19', '19'), ('24', '24')], default='24', max_length=2)),
                ('renew', models.SmallIntegerField(choices=[(1, 'Thứ nhất'), (0, 'Thứ hai')], default=0)),
                ('power_type', models.CharField(choices=[('10', '10'), ('5', '5'), ('2', '2')], default='5', max_length=2)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('machine_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='machine_locations.MachineLocation')),
            ],
            options={
                'db_table': 'unit_prices',
            },
        ),
    ]