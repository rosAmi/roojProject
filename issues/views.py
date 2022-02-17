from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from .models import Issue
from .serializers import IssuesSerializer


class IssuesViewSet(ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssuesSerializer


"""
def index(request):
    issues = []

    for issue in Issue.objects.all():
        issues.append({
            'uid': issue.uid,
            'description': issue.description,
            'serial': issue.serial,
            'indicator1': issue.indicator1,
            'indicator2': issue.indicator2,
            'indicator3': issue.indicator3,
            'date_time': issue.date_time,
            'response': issue.resolve,
        })
    return JsonResponse(issues, safe=False)
"""
