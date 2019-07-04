from django.db import models

class sprint(models.Model):
    Duration = models.DurationField()
    DeadLine = models.DateField()
    StartTime = models.DateField()
    InProgress = models.BooleanField()
    ProjectID = models.ForeignKey('project.Scrum',on_delete=models.CASCADE,related_name='%(class)s_requests_created',null=True)
