# Generated by Django 4.1.6 on 2023-03-06 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbasubmission', '0003_application_employer_application_job_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='phone_number',
            field=models.IntegerField(default=7118246),
            preserve_default=False,
        ),
    ]
