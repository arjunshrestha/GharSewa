# Generated by Django 3.2 on 2021-06-20 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210620_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookservice',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='bookservice',
            name='email',
            field=models.EmailField(default='', max_length=20),
        ),
    ]
