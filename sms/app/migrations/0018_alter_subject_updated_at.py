# Generated by Django 4.1.3 on 2022-12-21 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_attendance_attendance_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
