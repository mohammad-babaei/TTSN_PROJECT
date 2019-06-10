from django.db import models

class Backlog(models.Model):
    name = models.TextField(max_length=50)
    priority = models.IntegerField(unique=True)
    definition_done = models.TextField(max_length=150)
    description = models.TextField(max_length=150)
    create_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
