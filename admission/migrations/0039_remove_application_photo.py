# Generated by Django 4.1.6 on 2023-11-30 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0038_alter_application_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='photo',
        ),
    ]