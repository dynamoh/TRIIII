# Generated by Django 2.2.10 on 2020-05-13 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_is_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='area_of_expertise',
            field=models.CharField(choices=[('Other', 'Other'), ('Electricity', 'Electricity'), ('Workforce Management', 'Workforce Management'), ('Logistics', 'Logistics'), ('Technology', 'Technology'), ('Process and Quality', 'Process and Quality')], default='Other', max_length=100),
        ),
    ]
