# Generated by Django 2.1.7 on 2019-03-18 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_company_profile_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_profile',
            old_name='second_name',
            new_name='last_name',
        ),
    ]