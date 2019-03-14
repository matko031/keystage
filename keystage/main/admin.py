from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, student_profile, company_internship, took_internship





class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(student_profile)
admin.site.register(company_internship)
admin.site.register(took_internship)


"""
class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {"fields":["tutorial_title", "tutorial_published"]}),
        ("URL", {"fields":["tutorial_slug"]}),
        ("Series", {"fields":["tutorial_series"]}),
        ("Content", {"fields":["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }


admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory )
admin.site.register(profile_categories)
"""

