# Generated by Django 4.1.3 on 2022-11-17 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_number',
            field=models.IntegerField(default='0'),
        ),
    ]