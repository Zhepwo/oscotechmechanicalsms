# Generated by Django 4.1.3 on 2022-12-27 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_studentresult_total_marks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentresult',
            name='total_marks',
        ),
    ]
