from django.shortcuts import render
from .models import Department, Team, Dependency

def organisation_view(request):
    departments = Department.objects.all()
    teams = Team.objects.all()
    dependencies = Dependency.objects.all()

    return render(request, 'organisation/organisation.html', {
        'departments': departments,
        'teams': teams,
        'dependencies': dependencies
    })