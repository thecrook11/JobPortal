# Generated by Django 4.1.5 on 2023-01-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_applylist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('msg', models.CharField(max_length=500)),
            ],
        ),
    ]
