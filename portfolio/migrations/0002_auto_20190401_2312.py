# Generated by Django 2.1.7 on 2019-04-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='urlDemo',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='urlGit',
            field=models.URLField(blank=True, null=True),
        ),
    ]
