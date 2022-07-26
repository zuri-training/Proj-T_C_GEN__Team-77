# Generated by Django 4.0.6 on 2022-08-11 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terms77', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companies',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='companies',
            name='business_platform',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='companies',
            name='company_name',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='companies',
            name='company_website',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='companies',
            name='product_service',
            field=models.TextField(default='', max_length=50),
        ),
    ]
