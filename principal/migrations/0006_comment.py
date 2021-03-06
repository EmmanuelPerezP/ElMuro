# Generated by Django 2.0.7 on 2018-07-16 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_auto_20180715_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.BigIntegerField(default=0)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('commentText', models.CharField(max_length=10000)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Post')),
            ],
        ),
    ]
