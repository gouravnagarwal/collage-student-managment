# Generated by Django 5.0.1 on 2024-06-21 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('percentage', models.IntegerField()),
            ],
        ),
    ]
