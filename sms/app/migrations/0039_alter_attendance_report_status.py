# Generated by Django 4.1.3 on 2022-12-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_remove_studentresult_total_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_report',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
