from django.contrib import admin
from todo.models import Project, todo

# Register your models here.

@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'repository')

@admin.register(todo)
class todoModelAdmin(admin.ModelAdmin):
    list_display = ('body', 'project', 'user', 'activity')