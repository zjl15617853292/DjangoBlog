# Generated by Django 3.0.8 on 2020-07-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200720_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='avatar',
            field=models.ImageField(blank=True, default='/static/avator/title.png', upload_to='media/article/%Y%m%d'),
        ),
    ]