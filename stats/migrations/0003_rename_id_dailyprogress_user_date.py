# Generated by Django 4.0.6 on 2022-08-25 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_dailyprogress_id_alter_dailyprogress_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailyprogress',
            old_name='id',
            new_name='user_date',
        ),
    ]