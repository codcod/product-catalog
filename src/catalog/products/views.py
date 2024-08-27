# pylint: disable=C0114,C0115,C0116
from django.shortcuts import render, get_object_or_404

from .models import Journey, Project


def index(request):
    projects = Project.objects.order_by('key')  # pylint: disable=E1101
    ctx = {'projects': projects}
    return render(request, 'products/index.html', ctx)

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'products/project_detail.html', {'project': project})


def journey_list(request):
    journeys = Journey.objects.order_by('-pub_date')[:5]  # pylint: disable=E1101
    ctx = {'journeys': journeys}
    return render(request, 'products/journey_list.html', ctx)

def journey_detail(request, journey_id):
    journey = get_object_or_404(Journey, pk=journey_id)
    return render(request, 'products/journey_detail.html', {'journey': journey})
