# Generated by Django 4.0.6 on 2022-08-04 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('NC', 'Not Completed'), ('DE', 'Deadline Expired'), ('C', 'Completed'), ('E', 'Empty')], default='E', max_length=2)),
                ('progress', models.CharField(default='0% Done', max_length=9)),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_list', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
