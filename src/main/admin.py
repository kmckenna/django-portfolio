from django.contrib import admin
from tinymce.widgets import TinyMCE
from adminsortable2.admin import SortableAdminMixin

from .models import WorkExperience, Section, Skill, Project, Specialization, \
    Navigation, Proficiency, Course, Source, Page, Technology, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['specialization_name', 'specialization_section', 'is_active']
    list_filter = ['specialization_section', 'is_active']
    search_fields = ['specialization_name', 'specialization_section__section_name']
    formfield_overrides = {
        Specialization.specialization_description: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }


@admin.register(Project)
class SortableProjectAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['project_name', 'project_section', 'is_active', 'sequence']
    list_filter = ['project_section', 'is_active']
    search_fields = ['project_name', 'project_section__section_name']

    filter_horizontal = ('project_skills',)  
    inlines = [ProjectImageInline]
    
    formfield_overrides = {
        Project.project_description: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }   

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['experience_role', 'experience_company_name', 'is_active', 'sequence']
    list_filter = ['is_active']
    search_fields = ['experience_role', 'experience_company_name']

    filter_horizontal = ('experience_skills',)  

    formfield_overrides = {
        WorkExperience.experience_description: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }
@admin.register(Skill)
class SortableSkillAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['skill_name', 'skill_section', 'skill_proficiency', 'is_active', 'sequence']
    list_filter = ['skill_section', 'skill_proficiency', 'is_active']
    search_fields = ['skill_name', 'skill_section__section_name', 'skill_proficiency__proficiency_name']

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['section_name', 'is_active', 'sequence']
    list_filter = ['is_active']
    search_fields = ['section_name']

@admin.register(Navigation)
class SortableNavigationAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['link_label', 'is_active', 'sequence']
    list_filter = ['is_active']
    search_fields = ['link_label']

@admin.register(Proficiency)
class SortableProficiencyAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['proficiency_name', 'proficiency_level', 'is_active', 'sequence']
    list_filter = ['proficiency_level', 'is_active']
    search_fields = ['proficiency_name']

@admin.register(Course)
class SortableCourseAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['course_name', 'course_specialization', 'is_active', 'sequence']
    list_filter = ['course_specialization', 'is_active']
    search_fields = ['course_name', 'course_specialization__specialization_name']
    formfield_overrides = {
        Course.course_description: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

@admin.register(Source)
class SortableSourceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['source_name', 'source_link', 'is_active', 'sequence']
    list_filter = ['is_active']
    search_fields = ['source_name', 'source_link']
    formfield_overrides = {
        Source.source_description: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

@admin.register(Page)
class SortablePageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['page_title', 'page_slug', 'page_navigation', 'is_active', 'sequence']
    list_filter = ['page_navigation', 'is_active']
    search_fields = ['page_title', 'page_slug', 'page_navigation__link_label']
    formfield_overrides = {
        Page.page_content: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

@admin.register(Technology)
class SortableTechnologyAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['technology_name', 'technology_icon_class', 'is_active', 'sequence']