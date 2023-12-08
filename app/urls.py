from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("bot/", bot, name="bot"),
    path("intent_analysis/", analyse_intent, name="intent_analysis"),
    path('music/', listen_music, name='music'),
    
]
