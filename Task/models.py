from django.db import models

# from accounts.models import users

# from backlog.models import backlog

# from sprint.models import sprint

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    TaskState = models.IntegerField()
    picker = models.ForeignKey('accounts.users',on_delete=models.CASCADE)
    BackLogID = models.ForeignKey('Backlog.Backlog',on_delete=models.CASCADE)
    # SprintID = models.ForeignKey('sprint',on_delete=models.CASCADE)
