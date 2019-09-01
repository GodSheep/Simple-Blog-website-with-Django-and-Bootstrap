# Generated by Django 2.2.1 on 2019-08-24 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Tag',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='Category',
            field=models.CharField(blank=True, choices=[('life', '生活'), ('study', '学习'), ('stuff', '碎念'), ('aboutme', '关于')], max_length=50),
        ),
    ]
