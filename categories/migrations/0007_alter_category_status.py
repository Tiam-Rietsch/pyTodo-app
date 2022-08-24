# Generated by Django 4.0.6 on 2022-08-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0006_alter_category_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('2-OP', 'On progress'), ('3-C', 'Completed'), ('1-E', 'Empty')], default='1-E', max_length=4),
        ),
    ]
