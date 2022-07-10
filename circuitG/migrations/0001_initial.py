# Generated by Django 4.0.3 on 2022-06-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('otp', models.IntegerField(max_length=7)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('number', models.CharField(max_length=15)),
            ],
        ),
    ]
