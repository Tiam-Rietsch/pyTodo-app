# Generated by Django 4.0.6 on 2022-08-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_task_dead_line'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dead_line',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
