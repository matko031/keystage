from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from datetime import datetime
from django.core.validators import MaxValueValidator


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    type = models.CharField(max_length=1, choices=(('c','company'), ('s','student')))
    address = models.CharField(max_length=100)


class student_profile(models.Model):
    student = models.ForeignKey(CustomUser, default=None, on_delete=models.SET_DEFAULT)
    faculty = models.CharField(max_length=200)
    study_year = models.IntegerField(validators=[MaxValueValidator(10)])
    interests = models.CharField(max_length=1000)
    cv = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.CharField(max_length=50)
    internship_period = models.DateTimeField()



class company_internship(models.Model):
    name = models.CharField(max_length=100)
    target_faculty = models.CharField(max_length=100)
    internship_period = models.DateTimeField()
    target_study_year = models.IntegerField()
    company = models.ForeignKey(CustomUser, default = None, on_delete=models.SET_DEFAULT)


class took_internship(models.Model):
    student = models.ForeignKey(CustomUser, default = None, on_delete=models.SET_DEFAULT)
    internship = models.ForeignKey(company_internship, default=None, on_delete=models.SET_DEFAULT)





"""
class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)


    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published", default=datetime.now())

    tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.tutorial_title
"""
