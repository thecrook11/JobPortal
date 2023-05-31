# Generated by Django 4.1.5 on 2023-01-06 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='country',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='candidate',
            name='experience',
            field=models.CharField(default=0, max_length=150),
        ),
        migrations.AddField(
            model_name='candidate',
            name='highestEdu',
            field=models.CharField(default=0, max_length=150),
        ),
        migrations.AddField(
            model_name='candidate',
            name='jobCategory',
            field=models.CharField(default=0, max_length=150),
        ),
        migrations.AddField(
            model_name='candidate',
            name='jobDesc',
            field=models.CharField(default=0, max_length=150),
        ),
        migrations.AddField(
            model_name='candidate',
            name='jobType',
            field=models.CharField(default=0, max_length=150),
        ),
        migrations.AddField(
            model_name='candidate',
            name='maxSalary',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='candidate',
            name='minSalary',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='candidate',
            name='shift',
            field=models.CharField(default=0, max_length=150),
        ),
        migrations.AddField(
            model_name='candidate',
            name='website',
            field=models.CharField(default=0, max_length=150),
        ),
    ]
