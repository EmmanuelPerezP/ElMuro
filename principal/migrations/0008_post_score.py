# Generated by Django 2.0.7 on 2018-07-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_post_dislike'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
