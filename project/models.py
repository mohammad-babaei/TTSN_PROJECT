from django.db import models
from accounts.models import users
# class Project(models.Model):
#     MethodologyChoices = (
#         ("Scrum","scrum"),
#         ("Waterfall","waterfall"),
#         ("ExtremePrograming","extreme programing")
#     )
#     Methodology = models.CharField(max_length=20, choices=MethodologyChoices)
    


class Scrum(models.Model):
    Name = models.CharField(max_length=100)
    CreationDate = models.DateField(auto_now_add=True)
    StartDate = models.DateField()
    EndTime = models.DateField()
    Creator = models.ForeignKey('accounts.users',on_delete=models.SET_NULL,related_name='creater_assigned',null=True)
    TeamMembers = models.ManyToManyField(users,related_name='team_members_assigned',blank=True)
    ScrumMaster = models.ForeignKey('accounts.users',on_delete=models.SET_NULL,related_name='scrum_master_assigned',null=True,blank=True)
    ProjectManager = models.ForeignKey('accounts.users',on_delete=models.SET_NULL,related_name='project_manager_assigned',null=True,blank=True)
