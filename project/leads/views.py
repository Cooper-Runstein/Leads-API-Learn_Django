from django.shortcuts import render
from leads.models import leads
from leads.serializers import LeadSerializer
from rest_framework import generics

# Create your views here.
class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer