# Generated by Django 3.2.8 on 2021-10-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='default.svg', upload_to='articles/'),
        ),
    ]
