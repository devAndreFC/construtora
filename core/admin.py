from django.contrib import admin
from .models import Engineeer, Material, Project, ProjectMaterial

admin.site.register(Engineeer)
admin.site.register(Material)
admin.site.register(Project)
admin.site.register(ProjectMaterial)
