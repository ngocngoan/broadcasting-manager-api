# Generated by Django 2.0.1 on 2018-01-24 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('broadcasts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BroadcastingStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('power_T', models.CharField(blank=True, max_length=10, null=True)),
                ('power_PX', models.CharField(blank=True, max_length=10, null=True)),
                ('reporter', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('broadcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='broadcasts.Broadcast')),
            ],
            options={
                'db_table': 'broadcasting_status',
            },
        ),
    ]
