# Generated by Django 3.2.6 on 2021-08-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='first_name',
            new_name='caption_1',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='last_name',
            new_name='caption_2',
        ),
        migrations.AddField(
            model_name='image',
            name='caption_3',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='caption_4',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='caption_5',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
