# Generated by Django 3.1.5 on 2021-04-05 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/1439536495-1.png', upload_to='images/'),
        ),
    ]
