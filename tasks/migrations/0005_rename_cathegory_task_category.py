# Generated by Django 4.0.6 on 2022-08-04 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_remove_task_category_task_cathegory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='cathegory',
            new_name='category',
        ),
    ]
