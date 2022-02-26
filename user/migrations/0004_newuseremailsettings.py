# Generated by Django 4.0.1 on 2022-02-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUserEmailSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=25)),
                ('message', models.TextField()),
                ('from_mail', models.EmailField(max_length=50, verbose_name='From Mail')),
            ],
        ),
    ]
