from django.db import models
from authapp.models import PortalUser

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length = 128, unique=True, verbose_name = 'Project name')
    repository = models.URLField(max_length=256, unique=True, verbose_name = 'Project repository')
    user = models.ManyToManyField(PortalUser)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('name',)

    def __str__(self):
        return self.name

class todo(models.Model):
    body = models.TextField(max_length=1024, verbose_name = 'Note body')
    activity = models.BooleanField(default = True, verbose_name ='Activity status')
    user = models.ForeignKey(PortalUser, on_delete = models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True, editable = False, verbose_name = 'Date created')
    updated = models.DateTimeField(auto_now = True, editable = False, verbose_name = 'Date updated')

    class Meta:
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDos'
        ordering = ('-created',)

    def __str__(self):
        return f"{self.id}-{self.project}-{self.user.username}"