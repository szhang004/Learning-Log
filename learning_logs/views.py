# takes data through request and uses it to generate a page to send to the browser
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Topic, Entries
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request): # index is the home page
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # querying the database
    context = {'topics': topics} # dictionary in which key is 'topics' and values are the topics
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entries_set.order_by('-date_added') # minus sign indicates reverse order       
        # make sure whatever_set has the same name as the model 
    if topic.owner != request.user:
        raise Http404
    
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        # if No data is submitted
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False) # so that it doesn't save immediately
            new_topic.owner = request.user #gets user id
            new_topic.save()
            return HttpResponseRedirect(reverse('topics')) #redirects after submission
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):

    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) # commit=False to create new object w/o saving to database before adding topic
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):

    entry = Entries.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form=EntryForm(instance=entry) # basically prefilling w/ previous information 
    else:
        form=EntryForm(instance=entry, data=request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    
    context = {'entry':entry, 'topic':topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)