# Generated by Django 3.1.4 on 2021-05-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer_info', '0002_auto_20210529_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='address',
            field=models.TextField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='contact',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]