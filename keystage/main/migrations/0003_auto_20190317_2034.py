# Generated by Django 2.1.7 on 2019-03-17 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_student_profile_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_profile',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]