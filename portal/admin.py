from django.contrib import admin
from .models import Organization, Department, Team, TeamType

admin.site.register(Organization)
admin.site.register(Department)
admin.site.register(Team)
admin.site.register(TeamType)