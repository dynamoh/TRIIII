# Generated by Django 2.2.10 on 2020-05-24 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostChallenge', '0026_auto_20200523_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=4000),
        ),
        migrations.AlterUniqueTogether(
            name='blog',
            unique_together={('title', 'datePosted')},
        ),
    ]
