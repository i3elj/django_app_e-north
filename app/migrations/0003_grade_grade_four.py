# Generated by Django 4.0.6 on 2022-07-08 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_student_born_at_student_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='grade_four',
            field=models.FloatField(default=0.0),
        ),
    ]
