# Generated by Django 3.2.3 on 2021-06-17 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crochetApp', '0003_auto_20210617_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='totalPrice',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='product',
            name='itemPrice',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
