from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import WorkExperience, Section, Skill, Project, Specialization, Navigation, Proficiency, Course, Source


# class IndexView(generic.ListView):
#     template_name = "main/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by("-pub_date")[:5]


def curriculum_overview(request):
    sections = Section.objects.prefetch_related(
        'specializations__courses',
        'specializations__source',
    )

    return render(request, 'main/overview.html', {
        'sections': sections,
    })


def index(request):
    return render(request, 'main/index.html')
