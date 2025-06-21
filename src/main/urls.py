from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path("", TemplateView.as_view(template_name="index.html")),
    path(r"portfolio", TemplateView.as_view(template_name="portfolio.html")),
    path("skills", TemplateView.as_view(template_name="skills.html")),
    path("experience", TemplateView.as_view(template_name="experience.html")),
    path("education", TemplateView.as_view(template_name="education.html")),
    # path("", views.index, name="index"),
]