# Generated by Django 4.1.6 on 2023-04-28 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_campus_alter_course_duration_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Unit Code')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]