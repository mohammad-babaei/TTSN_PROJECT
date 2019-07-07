from django.db import models
from accounts.models import users
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.conf import settings
# class Project(models.Model):
#     MethodologyChoices = (
#         ("Scrum","scrum"),
#         ("Waterfall","waterfall"),
#         ("ExtremePrograming","extreme programing")
#     )
#     Methodology = models.CharField(max_length=20, choices=MethodologyChoices)


class ProjectUserInvitationModel(models.Model):
    email = models.OneToOneField('accounts.users',to_field='email', unique=True, on_delete=models.CASCADE,related_name='email_of_user')
    accepted = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    Project = models.ForeignKey("Project", on_delete=models.CASCADE)
    key = models.CharField(max_length=64,unique = True)
    sent = models.DateTimeField(null=True)
    inviter = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True,to_field='username', on_delete=models.CASCADE,related_name='inviter_of_user')

    # @classmethod
    # def save(self, *args, **kwargs):
    #     key2 = get_random_string(64).lower()
    #     self.key = key2
    #     super().save(*args, **kwargs)



# class Scrum(models.Model):
#     Name = models.CharField(max_length=100)
#     CreationDate = models.DateField(auto_now_add=True)
#     StartDate = models.DateField(blank=True, null=True)
#     EndTime = models.DateField()
#     Creator = models.ForeignKey(
#         'accounts.users', on_delete=models.SET_NULL, related_name='creater_assigned', null=True)
#     TeamMembers = models.ManyToManyField(
#         users, related_name='team_members_assigned', blank=True)
#     ScrumMaster = models.ForeignKey('accounts.users', on_delete=models.SET_NULL,
#                                     related_name='scrum_master_assigned', null=True, blank=True)
#     ProjectManager = models.ForeignKey(
#         'accounts.users', on_delete=models.SET_NULL, related_name='project_manager_assigned', null=True, blank=True)


class Project(models.Model):
    Name = models.CharField(max_length=100)
    CreationDate = models.DateField(auto_now_add=True)
    StartDate = models.DateField(blank=True, null=True)
    EndDate = models.DateField()
    Description = models.CharField(max_length=150,null=True)
    TypeChoices = (
        ("B2B","business to business"),
        ("C2C","customer to customer"),
        ("B2C","business to customer")
    )
    Type = models.CharField(max_length=20, choices=TypeChoices)
    MethodologyChoices = (
        ("Scrum","scrum"),
        ("Waterfall","waterfall"),
        ("XP","xp")
    )
    Methodology = models.CharField(max_length=20, choices=MethodologyChoices)
    Creator = models.ForeignKey(
        'accounts.users', on_delete=models.SET_NULL, related_name='creater_assigned', null=True)
