# Generated by Django 3.2.15 on 2023-07-08 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0003_auto_20230706_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page_element',
            name='question',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='page_element', to='qa.question'),
        ),
    ]
