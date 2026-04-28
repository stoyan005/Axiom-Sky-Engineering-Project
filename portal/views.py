from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Organization


def auth_page(request):
    return render(request, "portal/auth.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("auth")
    else:
        form = UserCreationForm()

    return render(request, "portal/signup.html", {"form": form})


@login_required
def home(request):
    orgs = Organization.objects.all()
    return render(request, "portal/home.html", {"orgs": orgs})


@login_required
def organization_list(request):
    query = request.GET.get("q", "").strip()

    orgs = Organization.objects.prefetch_related(
        "department_set__team_set__dependencies"
    )

    if query:
        orgs = orgs.filter(
            Q(name__icontains=query)
            | Q(department__name__icontains=query)
            | Q(department__team__name__icontains=query)
            | Q(department__team__dependencies__name__icontains=query)
        ).distinct()

    return render(
        request,
        "portal/organization_list.html",
        {
            "orgs": orgs,
            "query": query,
        },
    )
