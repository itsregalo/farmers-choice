from django.shortcuts import render
from .models import *
from .forms import IssueSolutionForm
from django.conf import settings
# Create your views here.
from user.models import User

from django.views.generic import ListView



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

    if request.method == 'POST' and request.user.is_authenticated:
        form = IssueSolutionForm(request.POST, request.FILES)
        if form.is_valid():
            issue_solution = form.save(commit=False)
            issue_solution.farmer = request.user
            issue_solution.issue = issue
            issue_solution.save()
            return render(request, 'issue_detail.html', {
                'issue': issue, 
                'issues': issues, 
                'categories': categories}
                )    

    context = {
        'issue': issue,
        'issues': issues,
        'categories': categories
    }
    return render(request, 'issue_detail.html', context)


def aboutus(request, *args, **kwargs):
    experts = User.objects.filter(is_staff=True)
    context = {
        'experts': experts
    }
    return render(request, 'about.html', context)
