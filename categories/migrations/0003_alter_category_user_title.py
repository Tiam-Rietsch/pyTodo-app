# Generated by Django 4.0.6 on 2022-08-05 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_user_title_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='user_title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
