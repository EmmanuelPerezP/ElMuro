# Generated by Django 2.0.7 on 2018-07-30 22:15

from django.db import migrations, models
import principal.models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_post_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to=principal.models.directory_path_images)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]