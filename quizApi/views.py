from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Pregunta
from .serializer import PreguntaSerializer


@api_view(['GET'])
def get_questions(request):
    questions = Pregunta.objects.all()
    serializedData = PreguntaSerializer(questions, many=True).data
    return Response(serializedData)

@api_view(['GET'])
def get_json(request):
    questions = Pregunta.objects.all()
    serializedData = PreguntaSerializer(questions, many=True).data
    qObj={}
    qObj["questions"]=serializedData
    return Response(qObj)
