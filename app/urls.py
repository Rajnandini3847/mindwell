from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("bot/", bot, name="bot"),
    path("intent_analysis/", analyse_intent, name="intent_analysis"),
    path('music/', listen_music, name='music'),
    path('dashboard/',dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('',login_view, name='login'),
    path('playlist/',playlist, name='playlist'),
    path('avatar/',avatar, name='avatar'),
    path('task/',task, name='task'),
    path('survey/',survey, name='survey'),
    path('notification/',notification, name='notification'),
    path('congrats/',congrats, name='congrats'),
    path("dynamic_task/", dynamic_tasks, name="dynamic_task"),
    
]
