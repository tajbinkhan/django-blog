# Generated by Django 4.0.1 on 2022-03-06 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_delete_commentformnotification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='next_post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='previous_post',
        ),
    ]
