from django.db import models

Choice = {'DRAFT': 'Draft',
          'IN PROGRESS': 'in progress',
          'COMPLETED': 'completed'}


class Task(models.Model):
    name = models.TextField()
    status = models.CharField(choices=Choice, max_length=100)
    description = models.TextField()