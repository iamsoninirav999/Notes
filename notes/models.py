from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

    def __str__(self):
        return self.username+' : '+self.email


class Label(models.Model):
    label=models.CharField(max_length=100)
    users_label=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_labels")

    def __str__(self):
        return self.label
    


class Note(models.Model):
    users_note=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_notes")
    title=models.CharField(max_length=100)
    note=models.TextField()
    archive=models.BooleanField(default=False)
    label=models.ManyToManyField(Label,blank=True,related_name="labled_notes")

    def __str__(self):
        return self.note+' by '+f'{self.users_note.username}'

