# Generated by Django 3.2.3 on 2021-06-16 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crochetApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zipCode',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
