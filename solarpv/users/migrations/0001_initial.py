# Generated by Django 3.1.2 on 2021-02-26 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('passwd', models.CharField(max_length=100)),
                ('conpasswd', models.CharField(max_length=100)),
                ('fName', models.CharField(max_length=100)),
                ('mName', models.CharField(max_length=100)),
                ('lName', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zipCode', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('cellPhone', models.CharField(max_length=15)),
                ('company', models.CharField(max_length=100)),
            ],
        ),
    ]
