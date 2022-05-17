from django.shortcuts import render
from user.models import User
from .models import *
# Create your views here.


def IndexView(request, *args, **kwargs):
    return render(request, 'index.html')

def issues(request, *args, **kwargs):
    issues = Issue.objects.all()
    context = {
        'issues': issues
    }
    return render(request, 'issues.html', context)

def issue_detail(request, slug, *args, **kwargs):
    categories = IssueCategory.objects.all()
    issue = Issue.objects.get(slug=slug)
    issues = Issue.objects.all()[:3]
    context = {
        'issue': issue,
        'issues': issues,
        'categories': categories
    }
    return render(request, 'issue_detail.html', context)


def aboutus(request, *args, **kwargs):
    experts = User.objects.filter(is_farmer=True)
    context = {
        'experts': experts
    }
    return render(request, 'about.html', context)
