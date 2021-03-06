# Generated by Django 2.1.7 on 2019-03-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20190322_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_internships',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='company_internships',
            name='internship_period',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='company_internships',
            name='target_faculty',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company_internships',
            name='target_study_year',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
