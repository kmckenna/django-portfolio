from django.db import models


class Navigation(models.Model):
    link_label = models.TextField(max_length=50)
    link_reference = models.TextField(max_length=50, blank=True, null=True)
    link_sequence = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_home = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.link_label}-{self.link_sequence}"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WorkExperience(models.Model):
    experience_role = models.TextField(max_length=200)
    experience_company_name = models.TextField(max_length=200)
    experience_dates = models.TextField(max_length=200)
    experience_description = models.TextField(max_length=4000) 
    experience_sequence = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.experience_role} at {self.experience_company_name}-{self.experience_sequence}"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Proficiency(models.Model):
    proficiency_name = models.TextField(max_length=100)
    proficiency_level = models.IntegerField(default=0)
    proficiency_sequence = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.proficiency_name} (Level {self.proficiency_level})-{self.proficiency_sequence}"

    class Meta:
        verbose_name_plural = "proficiencies"    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Section(models.Model):
    section_name = models.TextField(max_length=100)
    section_sequence = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.section_name}-{self.section_sequence}"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Skill(models.Model):
    skill_name = models.TextField(max_length=100)
    skill_proficiency = models.ForeignKey(Proficiency, on_delete=models.CASCADE, related_name='skills', null=True, blank=True)
    skill_sequence = models.IntegerField(default=0)
    skill_section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return f"Section {self.skill_section} {self.skill_name} (Level {self.skill_proficiency})-{self.skill_sequence}"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   




class Project(models.Model):
    project_name = models.TextField(max_length=200)
    project_description = models.TextField(max_length=4000)
    project_link = models.TextField(max_length=200)

    project_sequence = models.IntegerField(default=0)
    # Foreign key to ProjectSection
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return f"{self.project_name} (Sequence: {self.project_sequence})"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Source(models.Model):
    source_name = models.TextField(max_length=200)
    source_link = models.TextField(max_length=200, blank=True, null=True)
    source_description = models.TextField(max_length=4000, blank=True, null=True)
    source_sequence = models.IntegerField(default=0)
    source_parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    # Foreign key to Section
    # section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='sources')

    def __str__(self):
        return f"{self.source_name} ({self.source_sequence})"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Specialization(models.Model):
    specialization_name = models.TextField(max_length=200)
    specialization_link = models.TextField(max_length=200)
    specialization_description = models.TextField(max_length=4000, blank=True, null=True)
    specialization_completion_date = models.DateField(blank=True, null=True)
    specialization_sequence = models.IntegerField(default=0)
    # Foreign key to Section
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='specializations')
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='specializations', null=True)

    def __str__(self):
        return f"{self.specialization_name} (Sequence: {self.specialization_sequence})"

    # Assuming a specialization can exist without a section, using `null=True`
    # If you want to enforce that every specialization must have a section, remove `null=True`
    # section = models.ForeignKey(ProjectSection, on_delete=models.CASCADE, related_name='specializations', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    course_name = models.TextField(max_length=200)
    course_link = models.TextField(max_length=200)
    course_description = models.TextField(max_length=4000)
    course_completion_date = models.DateField(blank=True, null=True)
    course_sequence = models.IntegerField(default=0)
    # Foreign key to Specialization
    # This assumes that a course belongs to a specialization
    # A course can exist without a specialization, using `null=True`
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='courses', null=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='courses', null=True)

    def __str__(self):
        return f"{self.course_name} (Sequence: {self.course_sequence} in {self.specialization})"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
