# Generated by Django 4.1.5 on 2023-01-10 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_jobdetails_companyid_jobdetails_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetailsComp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobName', models.CharField(max_length=250)),
                ('companyName', models.CharField(max_length=250)),
                ('companyAddress', models.CharField(max_length=250)),
                ('jobDescComp', models.CharField(max_length=250)),
                ('qualification', models.CharField(max_length=250)),
                ('responsibilties', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('companyWebsite', models.CharField(max_length=250)),
                ('companyEmail', models.CharField(max_length=250)),
                ('companyContact', models.CharField(max_length=20)),
                ('salaryPackage', models.CharField(max_length=250)),
                ('experience', models.IntegerField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usermaster')),
            ],
        ),
        migrations.DeleteModel(
            name='JobDetails',
        ),
    ]