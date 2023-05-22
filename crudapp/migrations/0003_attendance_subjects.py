# Generated by Django 4.2.1 on 2023-05-22 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_attendance_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='subjects',
            field=models.CharField(choices=[('CIT511', 'CIT511'), ('CBS402A', 'CBS402A'), ('GEE002B', 'GEE002B')], default='CIT511', max_length=10),
        ),
    ]
