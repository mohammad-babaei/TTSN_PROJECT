from django.shortcuts import render
from rest_framework import viewsets
from Backlog.serializers import BacklogSerializer
from Backlog.models import Backlog
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BacklogList(APIView):
    
    def get(self,request,format = None):
        Backlogs = Backlog.objects.all()
        serializer = BacklogSerializer(Backlogs,many = True)
        return(serializer.data)
    def post(self, request, format=None):
        serializer = BacklogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

