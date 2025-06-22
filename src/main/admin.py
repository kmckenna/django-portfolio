from django.contrib import admin
from tinymce.widgets import TinyMCE
from adminsortable2.admin import SortableAdminMixin

from .models import WorkExperience, Section, Skill, Project, Specialization, \
    Navigation, Proficiency, Course, Source, Page, Technology
# Register your models here.
admin.site.register(WorkExperience)
admin.site.register(Skill)
admin.site.register(Section)
admin.site.register(Project)
admin.site.register(Specialization)
admin.site.register(Navigation)
admin.site.register(Proficiency)
admin.site.register(Course)
admin.site.register(Source)
admin.site.register(Technology)
admin.site.register(Page)
