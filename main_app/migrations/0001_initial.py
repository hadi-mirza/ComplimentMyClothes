# Generated by Django 3.1.5 on 2021-02-02 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('tshirt', 'T-Shirt'), ('sweater', 'Sweater'), ('sweatshirt', 'Sweatshirt'), ('jacket', 'Jacket'), ('jeans', 'Jeans'), ('leggings', 'Leggings'), ('shorts', 'Shorts')], default='tshirt', max_length=10)),
                ('color', models.CharField(choices=[('Pink', 'Pink'), ('Red', 'Red'), ('Orange', 'Orange'), ('Beige', 'Beige'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Light Blue', 'Light Blue'), ('Dark Blue', 'Dark Blue'), ('Purple', 'Purple'), ('Brown', 'Brown'), ('Grey', 'Grey')], default='Pink', max_length=10)),
                ('season', models.CharField(choices=[('spring', 'Spring'), ('summer', 'Summer'), ('fall', 'Fall'), ('winter', 'Winter')], default='spring', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('clothing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.clothing')),
            ],
        ),
    ]
