from django.db import models
from tinymce.models import HTMLField

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    sequence = models.IntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['sequence']

class Navigation(BaseModel):
    link_label = models.TextField(max_length=50)
    link_reference = models.TextField(max_length=50, blank=True, null=True)
    link_sequence = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.link_label}-{self.sequence} Active: {self.is_active}"


class Page(BaseModel):
    page_title = models.TextField(max_length=200)
    page_slug = models.SlugField(max_length=200, unique=True)
    page_content = HTMLField()
    page_navigation = models.ForeignKey(Navigation, on_delete=models.CASCADE, related_name='pages', null=True, blank=True)

    def __str__(self):
        return f"{self.page_title}-{self.sequence} Active: {self.is_active}"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    sequence = models.IntegerField(default=0)

class WorkExperience(BaseModel):
    experience_role = models.TextField(max_length=200)
    experience_company_name = models.TextField(max_length=200)
    experience_dates = models.TextField(max_length=200)
    experience_description = HTMLField(max_length=4000) 

    def __str__(self):
        return f"{self.experience_role} at {self.experience_company_name}-{self.sequence} Active: {self.is_active}"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    sequence = models.IntegerField(default=0)

class Proficiency(BaseModel):
    proficiency_name = models.TextField(max_length=100)
    proficiency_level = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.proficiency_name} (Level {self.proficiency_level})-{self.sequence} Active: {self.is_active}"

    class Meta:
        verbose_name_plural = "proficiencies"    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    sequence = models.IntegerField(default=0)

class Section(BaseModel):
    section_name = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.section_name}-{self.section_sequence}"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    sequence = models.IntegerField(default=0)


class Skill(BaseModel):
    skill_name = models.TextField(max_length=100)
    skill_proficiency = models.ForeignKey(Proficiency, on_delete=models.CASCADE, related_name='skills', null=True, blank=True)
    skill_section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return f"Section {self.skill_section} {self.skill_name} (Level {self.skill_proficiency})-{self.skill_sequence} Active: {self.is_active}"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)  




class Project(BaseModel):
    project_name = models.TextField(max_length=200)
    project_description = HTMLField(max_length=4000)
    project_link = models.TextField(max_length=200)
    # Foreign key to ProjectSection
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return f"{self.project_name}-{self.project_sequence} Active: {self.is_active}   "

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    sequence = models.IntegerField(default=0)

class Source(BaseModel):
    source_name = models.TextField(max_length=200)
    source_link = models.TextField(max_length=200, blank=True, null=True)
    source_description = HTMLField(max_length=4000, blank=True, null=True)
    source_parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    # Foreign key to Section
    # section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='sources')

    def __str__(self):
        return f"{self.source_name}-{self.source_sequence} Active: {self.is_active}"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    sequence = models.IntegerField(default=0)

class Specialization(BaseModel):
    specialization_name = models.TextField(max_length=200)
    specialization_link = models.TextField(max_length=200)
    specialization_description = HTMLField(max_length=4000, blank=True, null=True)
    specialization_completion_date = models.DateField(blank=True, null=True)
    # Foreign key to Section
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='specializations')
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='specializations', null=True)

    def __str__(self):
        return f"{self.specialization_name}-{self.specialization_sequence} Active: {self.is_active}"

    # Assuming a specialization can exist without a section, using `null=True`
    # If you want to enforce that every specialization must have a section, remove `null=True`
    # section = models.ForeignKey(ProjectSection, on_delete=models.CASCADE, related_name='specializations', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    sequence = models.IntegerField(default=0)

class Course(BaseModel):
    course_name = models.TextField(max_length=200)
    course_link = models.TextField(max_length=200)
    course_description = HTMLField(max_length=4000)
    course_completion_date = models.DateField(blank=True, null=True)
    # Foreign key to Specialization
    # This assumes that a course belongs to a specialization
    # A course can exist without a specialization, using `null=True`
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='courses', null=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='courses', null=True)

    def __str__(self):
        return f"{self.course_name}-{self.sequence} in {self.specialization} Active: {self.is_active}"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    sequence = models.IntegerField(default=0)

class Technology(BaseModel):
    technology_name = models.TextField(max_length=100)
    technology_icon_class = models.TextField(max_length=100)
    technology_description = HTMLField(max_length=4000, blank=True, null=True)

    def __str__(self):
        return f"{self.technology_name}-{self.sequence} Active: {self.is_active}"

    class Meta:
        verbose_name_plural = "technologies"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    sequence = models.IntegerField(default=0)