# Generated by Django 3.1.3 on 2021-02-05 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210204_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothing',
            name='season',
            field=models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall'), ('Winter', 'Winter')], default='Spring', max_length=10),
        ),
    ]
