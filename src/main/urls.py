from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path('', views.index, name='index'),
    path('curriculum/', views.curriculum_overview, name='curriculum'),
    path('skills/', views.skills_overview, name='skills'),
    path('projects/', views.projects_overview, name='projects'),
    # path("portfolio", TemplateView.as_view(template_name="portfolio.html")),
    # path("skills", TemplateView.as_view(template_name="skills.html")),
    # path("experience", TemplateView.as_view(template_name="experience.html")),
    # path("education", TemplateView.as_view(template_name="education.html")),
    # path("curriculum/", views.curriculum_overview, name="curriculum"),
    # path("", views.index, name="index"),
]