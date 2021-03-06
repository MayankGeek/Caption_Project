# Generated by Django 3.2.6 on 2021-08-11 16:38

from django.db import migrations, models
import index.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0009_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to=index.models.path_and_rename)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
