# Generated by Django 3.2.6 on 2021-08-10 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210810_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.jpg', null=True, upload_to=''),
        ),
    ]
