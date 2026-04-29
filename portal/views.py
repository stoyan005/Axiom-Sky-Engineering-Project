from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Team


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
def organization_list(request):
    query = request.GET.get("q", "").strip()
    team_id = request.GET.get("team_id")

    # DETAIL VIEW
    if team_id:
        selected_team = (
            Team.objects.select_related("department__organization")
            .prefetch_related("dependencies")
            .get(id=team_id)
        )

        return render(
            request,
            "portal/organization_list.html",
            {
                "selected_team": selected_team,
                "teams": None,
                "query": query,
            },
        )

    # LIST VIEW
    teams = Team.objects.select_related("department__organization")

    if query:
        teams = teams.filter(name__icontains=query)

    return render(
        request,
        "portal/organization_list.html",
        {
            "teams": teams,
            "selected_team": None,
            "query": query,
        },
    )
