from django.shortcuts import render
from .models import Team


def organization_list(request):
    query = request.GET.get("q", "").strip()
    team_id = request.GET.get("team_id")

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
