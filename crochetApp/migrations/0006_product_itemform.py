# Generated by Django 3.2.5 on 2021-07-12 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crochetApp', '0005_auto_20210617_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='itemForm',
            field=models.CharField(default='https://forms.gle/9TSjyGs3udM8Gya17', max_length=500),
        ),
    ]