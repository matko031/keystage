# Generated by Django 2.1.7 on 2019-03-31 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_account_categories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='account_categories',
            new_name='account_labels',
        ),
    ]