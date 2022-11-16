# Generated by Django 4.1.2 on 2022-10-24 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('post_date', models.DateField(auto_now=True)),
                ('tags', models.CharField(max_length=20)),
                ('image', models.ImageField(height_field=200, max_length=300, upload_to=None, width_field=300)),
                ('file_upload', models.FileField(upload_to=None)),
            ],
        ),
    ]
