from django.db import models

class sprint(models.Model):
    Duration = models.DurationField()
    DeadLine = models.DateField()
    StartTime = models.DateField()
    InProgress = models.BooleanField()
    # ProjectID = models.ForeignKey('Project.Project',on_delete=models.CASCADE)
