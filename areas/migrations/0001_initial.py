# Generated by Django 2.0.1 on 2018-01-24 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Tây Bắc', 'Tây Bắc'), ('Đông Bắc', 'Đông Bắc'), ('Đồng Bằng Sông Hồng', 'Đồng Bằng Sông Hồng'), ('Bắc Trung Bộ', 'Bắc Trung Bộ'), ('Nam Trung Bộ', 'Nam Trung Bộ'), ('Tây Nguyên', 'Tây Nguyên'), ('Đông Nam Bộ', 'Đông Nam Bộ'), ('Đồng Bằng Sông Cửu Long', 'Đồng Bằng Sông Cửu Long')], max_length=50)),
            ],
            options={
                'db_table': 'areas',
            },
        ),
    ]
