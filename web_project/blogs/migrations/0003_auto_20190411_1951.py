# Generated by Django 2.1.5 on 2019-04-11 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20190411_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='images',
        ),
        migrations.AlterField(
            model_name='image',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_images', to='blogs.Blog'),
        ),
    ]
