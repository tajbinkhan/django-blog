# Generated by Django 4.0.1 on 2022-03-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0013_alter_emailcontent_plain_text_html_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcontent',
            name='plain_text_html',
            field=models.TextField(verbose_name='Plain Text HTML'),
        ),
    ]
