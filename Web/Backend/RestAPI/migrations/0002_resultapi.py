# Generated by Django 5.0.3 on 2024-04-01 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultAPI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumberPeople', models.IntegerField()),
                ('Date', models.DateField()),
            ],
        ),
    ]