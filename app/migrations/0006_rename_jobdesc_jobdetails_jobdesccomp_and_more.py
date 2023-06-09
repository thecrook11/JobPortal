# Generated by Django 4.1.5 on 2023-01-10 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_jobdetails_companyid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobdetails',
            old_name='jobDesc',
            new_name='jobDescComp',
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='companyId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
    ]
