# Generated by Django 2.2.10 on 2020-04-29 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostChallenge', '0002_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='posted_by',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
    ]
