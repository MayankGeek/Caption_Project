# Generated by Django 3.2.6 on 2021-09-02 19:16

from django.db import migrations, models
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0018_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(max_length=255, upload_to=index.models.path_and_rename),
        ),
    ]
