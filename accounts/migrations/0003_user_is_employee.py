# Generated by Django 2.2.10 on 2020-05-10 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_gstin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=False),
        ),
    ]
