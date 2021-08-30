# Generated by Django 3.2.6 on 2021-08-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField(max_length=50)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
