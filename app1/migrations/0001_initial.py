# Generated by Django 3.1.2 on 2020-10-19 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('phone', models.IntegerField(max_length=12)),
                ('Address', models.TextField(max_length=100)),
            ],
        ),
    ]
