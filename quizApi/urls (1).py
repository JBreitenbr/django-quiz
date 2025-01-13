from django.urls import path
from .views import get_questions,get_json

urlpatterns = [
    path('questions/', get_questions, name='get_questions'),
    path('qjson/',get_json,name='get_json')
]