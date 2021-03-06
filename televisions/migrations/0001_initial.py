# Generated by Django 2.0.1 on 2018-01-24 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Television',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('province', models.CharField(max_length=50)),
                ('representative', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('fax', models.CharField(blank=True, max_length=15, null=True)),
                ('tax_code', models.CharField(blank=True, max_length=15, null=True)),
                ('bank_account', models.CharField(max_length=20)),
                ('bank', models.CharField(max_length=100)),
                ('decision_number', models.CharField(blank=True, max_length=20, null=True)),
                ('decision_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'televisions',
            },
        ),
    ]
