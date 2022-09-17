from django import forms

from .models import Topic, Entries

class TopicForm(forms.ModelForm): # more info on forms.ModelForm
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}
    # Django automatically adds this stuff into the database

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entries
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'col':80})}