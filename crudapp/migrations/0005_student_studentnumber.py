# Generated by Django 4.2.1 on 2023-05-16 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0004_student_address_student_age_student_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='studentnumber',
            field=models.TextField(default='', max_length=20),
        ),
    ]
