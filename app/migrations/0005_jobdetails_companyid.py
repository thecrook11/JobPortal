# Generated by Django 4.1.5 on 2023-01-10 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_jobdetails_alter_candidate_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetails',
            name='companyId',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
    ]
