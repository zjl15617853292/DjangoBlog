# Generated by Django 3.0.8 on 2020-07-20 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200719_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='categary',
            new_name='category',
        ),
    ]
