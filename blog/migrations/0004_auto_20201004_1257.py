# Generated by Django 3.0.8 on 2020-10-04 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200716_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='thumbnail',
            new_name='img_thumbnail',
        ),
    ]
