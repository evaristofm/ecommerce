# Generated by Django 3.1.5 on 2021-04-24 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210424_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='1439536495-1.png', upload_to='media/'),
        ),
    ]
