from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ProjectUser(AbstractUser):

    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'  # Setting email for default authentication
    REQUIRED_FIELDS = ['username']
    username = None


class ProjectTye(models.Model):
    type = models.CharField(max_length=50)

class ProjectTags(models.Model):
    tags = models.CharField(max_length=50)

class Project(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique=True)
    image = models.CharField(max_length=250)
    project_type = models.ForeignKey(ProjectTye, on_delete=models.CASCADE)
    project_tags = models.ManyToManyField(ProjectTags)
    body = models.CharField(max_length=2500)
