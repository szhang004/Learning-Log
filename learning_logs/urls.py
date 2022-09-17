from django.urls import path
from . import views

urlpatterns=[
    #your paths go here
    path('', views.index, name='index'), # home page
    path('topics/', views.topics, name='topics'), 
    path('topics/<int:topic_id>/', views.topic, name='topic'), # add id arguemnt since each entry is linked to topic by id
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
