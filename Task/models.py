from django.db import models

# from accounts.models import users

# from backlog.models import backlog

# from sprint.models import sprint

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    TaskChoices = (
        ("IN_PROGRESS","in progress"),
        ("TO_DO","to do"),
        ("DONE","done")
    )
    TaskState = models.CharField(max_length=12, choices=TaskChoices)
    picker = models.ForeignKey('accounts.users',on_delete=models.CASCADE,null=True)
    pair_picker = models.ForeignKey('accounts.users',related_name="pair_picker",on_delete=models.CASCADE,null=True)
    BackLogID = models.ForeignKey('Backlog.Backlog',on_delete=models.CASCADE)
    # SprintID = models.ForeignKey('sprint',on_delete=models.CASCADE)
