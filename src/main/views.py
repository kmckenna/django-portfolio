from django.db.models import F, Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import WorkExperience, Section, Skill, Project, Specialization, Navigation, Proficiency \
    , Course, Source, Technology


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

    section_icons = {
        'Programming': 'fa-solid fa-code',
        'Databases': 'fa-solid fa-database',
        'Security': 'fa-solid fa-shield-halved',
        'Web Design': 'fa-solid fa-palette',
        'Frameworks': 'fa-solid fa-cubes',
        'Tools & Workflow': 'fa-solid fa-screwdriver-wrench',
        'APIs & Integration': 'fa-solid fa-plug',
        'Data & Analytics': 'fa-solid fa-chart-line',
        'Cloud & Hosting': 'fa-solid fa-cloud',
    }

    return render(request, 'main/skills.html', {
        'sections': sections,
        'section_icons': section_icons,
    })

def projects_overview(request):
    sections = Section.objects.prefetch_related(
        Prefetch(
            'projects',
            queryset=Project.objects.filter(is_active=True)
                .order_by('sequence')
                .prefetch_related('project_skills')
                    .filter(is_active=True)
                    .order_by('sequence')
        )
    ).filter(is_active=True).order_by('sequence')

    return render(request, 'main/projects.html', {
        'sections': sections,
    })

def project_detail(request, id):
    project = get_object_or_404(
        Project.objects.prefetch_related('project_skills'),
        id=id,
        is_active=True
    )

    return render(request, 'main/project_detail.html', {
        'project': project,
    })


def experience_overview(request):
    workexperience = WorkExperience.objects.filter(is_active=True).order_by('sequence')


    return render(request, 'main/experience.html', {
        'workexperience': workexperience,
    })


