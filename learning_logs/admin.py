from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic, Entries

admin.site.register(Topic)
admin.site.register(Entries)