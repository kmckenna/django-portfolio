from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
from .models import WorkExperience, Section, Skill, Project, Specialization, Navigation, Proficiency, Course, Source

class WorkExperienceModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 20})}
    }

admin.site.register(WorkExperience, WorkExperienceModelAdmin)

# admin.site.register(WorkExperience)
admin.site.register(Skill)
admin.site.register(Section)
admin.site.register(Project)
admin.site.register(Specialization)
admin.site.register(Navigation)
admin.site.register(Proficiency)
admin.site.register(Course)
admin.site.register(Source)
