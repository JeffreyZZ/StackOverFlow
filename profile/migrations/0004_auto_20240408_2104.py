# Generated by Django 3.2.15 on 2024-04-09 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='not_to_Display_Full_name',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
