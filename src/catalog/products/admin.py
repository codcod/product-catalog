# pylint: disable=C0114,C0115,C0116
from django.contrib import admin

# Register your models here.
from .models import (
    Journey,
    Feature,
    SubFeature,
    Assignee,
    Team,
    Project,
    Version,
    Vendor
)

admin.site.register(Journey)
admin.site.register(Feature)
admin.site.register(SubFeature)
admin.site.register(Assignee)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(Version)
admin.site.register(Vendor)
