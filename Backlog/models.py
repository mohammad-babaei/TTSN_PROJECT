from django.db import models

class Backlog(models.Model):
    name = models.TextField(max_length=50)
    definition_done = models.TextField(max_length=150)
    description = models.TextField(max_length=150)
    create_date = models.DateField(auto_now=True)
    priority = models.IntegerField(blank=True, null=True)
    ProjectID = models.ForeignKey('project.Project',on_delete=models.CASCADE,related_name='%(class)s_requests_created',null=True)
    def __str__(self):
        return self.name
    # def save(self,*args,**kwargs):
    #     super(Backlog,self).save(*args,**kwargs)
    #     self.priority = self.id