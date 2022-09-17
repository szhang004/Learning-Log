from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)

    def __str__(self):
        return self.text    # returns the text part of it automatically

class Entries(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE) # Foreign Key is a reference to another object in Database (the Topic here)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:  # meta class just helps manage the class
        verbose_name_plural = 'entries' # just so it's entries and not entrys XD

    def __str__(self):
        return self.text[:50] + "..." 