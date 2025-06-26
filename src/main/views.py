from django.db.models import F, Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic




from .models import WorkExperience, Section, Skill, Project, Specialization, Navigation, Proficiency \
    , Course, Source, Technology


# class IndexView(generic.ListView):
#     template_name = "main/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by("-pub_date")[:5]

def index(request):
    what_i_do = Technology.objects.filter(is_active=True)
    return render(request, 'main/index.html', {
        'what_i_do': what_i_do
    })


def curriculum_overview(request):
    sections = Section.objects.prefetch_related(
        Prefetch(
            'specializations',
            queryset=Specialization.objects.filter(is_active=True).prefetch_related(
                Prefetch('courses', queryset=Course.objects.filter(is_active=True)),
                Prefetch('specialization_source', queryset=Source.objects.filter(is_active=True))
            )
        )
    ).filter(is_active=True).order_by('sequence')


    return render(request, 'main/curriculum.html', {
        'sections': sections,
    })

def skills_overview(request):
    sections = Section.objects.prefetch_related(
        Prefetch(
            'skills',
            queryset=Skill.objects.filter(is_active=True)
                .select_related('skill_proficiency')
                .order_by('sequence')
        )
    ).filter(is_active=True).order_by('sequence')

    return render(request, 'main/skills.html', {
        'sections': sections,
    })

def projects_overview(request):
    sections = Section.objects.prefetch_related(
        Prefetch(
            'projects',
            queryset=Project.objects.filter(is_active=True).order_by('sequence')
        )
    ).filter(is_active=True).order_by('sequence')


    return render(request, 'main/projects.html', {
        'sections': sections,
    })




