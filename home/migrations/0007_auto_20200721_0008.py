# Generated by Django 3.0.8 on 2020-07-20 16:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]