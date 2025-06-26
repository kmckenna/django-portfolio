from django.db import models
from tinymce.models import HTMLField

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    sequence = models.IntegerField(default=0)

    class Meta:
        abstract = True

class Navigation(BaseModel):
    link_label = models.TextField(max_length=50)
    link_reference = models.TextField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.link_label

    class Meta:
        ordering = ['sequence']

class Page(BaseModel):
    page_title = models.TextField(max_length=200)
    page_slug = models.SlugField(max_length=200, unique=True)
    page_content = HTMLField()
    page_navigation = models.ForeignKey(Navigation, on_delete=models.CASCADE, related_name='pages', null=True, blank=True)

    def __str__(self):
        return f"{self.page_title}-{self.sequence} Active: {self.is_active}"

    class Meta:
        ordering = ['sequence']

class WorkExperience(BaseModel):
    experience_role = models.TextField(max_length=200)
    experience_company_name = models.TextField(max_length=200)
    experience_dates = models.TextField(max_length=200)
    experience_description = HTMLField(max_length=4000) 

    def __str__(self):
        return self.experience_role


class Proficiency(BaseModel):
    proficiency_name = models.TextField(max_length=100)
    proficiency_level = models.IntegerField(default=0)

    def __str__(self):
        return self.proficiency_name

    class Meta:
        verbose_name_plural = "proficiencies"    
        ordering = ['sequence']

class Section(BaseModel):
    section_name = models.TextField(max_length=100)

    def __str__(self):
        return self.section_name


class Skill(BaseModel):
    skill_name = models.TextField(max_length=100)
    skill_proficiency = models.ForeignKey(Proficiency, on_delete=models.CASCADE, related_name='skills', null=True, blank=True)
    skill_section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return self.skill_name

    class Meta:
        ordering = ['sequence']

class Project(BaseModel):
    project_name = models.TextField(max_length=200)
    project_description = HTMLField(max_length=4000)
    project_link = models.TextField(max_length=200)
    # Foreign key to ProjectSection
    project_section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.project_name

    class Meta:
        ordering = ['sequence']

class Source(BaseModel):
    source_name = models.TextField(max_length=200)
    source_link = models.TextField(max_length=200, blank=True, null=True)
    source_description = HTMLField(max_length=4000, blank=True, null=True)
    source_parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def __str__(self):
        return self.source_name

    class Meta:
        ordering = ['sequence']

class Specialization(BaseModel):
    specialization_name = models.TextField(max_length=200)
    specialization_link = models.TextField(max_length=200)
    specialization_description = HTMLField(max_length=4000, blank=True, null=True)
    specialization_completion_date = models.DateField(blank=True, null=True)
    # Foreign key to Section
    specialization_section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='specializations')
    specialization_source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='specializations', null=True)

    def __str__(self):
        return self.specialization_name

    class Meta:
        ordering = ['sequence']

class Course(BaseModel):
    course_name = models.TextField(max_length=200)
    course_link = models.TextField(max_length=200)
    course_description = HTMLField(max_length=4000)
    course_completion_date = models.DateField(blank=True, null=True)
    # Foreign key to Specialization
    course_specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='courses', null=True)
    # source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='courses', null=True)

    def __str__(self):
        return self.course_name

    class Meta:
        ordering = ['sequence']

class Technology(BaseModel):
    technology_name = models.TextField(max_length=100)
    technology_icon_class = models.TextField(max_length=100)
    technology_description = HTMLField(max_length=4000, blank=True, null=True)

    def __str__(self):
        return self.technology_name

    class Meta:
        ordering = ['sequence']
        verbose_name_plural = "technologies"

 