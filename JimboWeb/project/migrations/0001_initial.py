# Generated by Django 4.1.2 on 2022-11-08 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='no titles', max_length=50)),
                ('project_date', models.CharField(default='no date', max_length=50)),
                ('category', models.CharField(default='no category', max_length=50)),
                ('personal_team_project', models.CharField(default='personal/team', max_length=50)),
                ('introduction_to_project', models.TextField(default='no intro')),
                ('github_link', models.URLField(default='no url')),
            ],
        ),
    ]