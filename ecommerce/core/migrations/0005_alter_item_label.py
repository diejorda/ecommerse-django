# Generated by Django 4.1.1 on 2022-10-26 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_category_item_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('p', 'primar-color'), ('s', 'secondary-color'), ('d', 'danger-color')], default='p', max_length=1),
        ),
    ]
