# Generated by Django 3.2 on 2021-06-26 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210622_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_man',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.service'),
        ),
    ]
