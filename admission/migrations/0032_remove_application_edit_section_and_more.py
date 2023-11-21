# Generated by Django 4.1.6 on 2023-11-21 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0031_alter_application_fifth_form_year_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='edit_section',
        ),
        migrations.AddField(
            model_name='application',
            name='furthest_section',
            field=models.CharField(choices=[('personal_details', 'Personal Details'), ('sponsor_details', 'Sponsor Details'), ('education_background', 'Education Background'), ('employment_history', 'Employment History'), ('declaration', 'Declaration')], default='personal_details', max_length=40, verbose_name='The furthest section that the user has reached.'),
        ),
        migrations.AlterField(
            model_name='application',
            name='current_section',
            field=models.CharField(choices=[('personal_details', 'Personal Details'), ('sponsor_details', 'Sponsor Details'), ('education_background', 'Education Background'), ('employment_history', 'Employment History'), ('declaration', 'Declaration')], default='personal_details', max_length=40, verbose_name='The section that is on edit by user (current).'),
        ),
    ]
