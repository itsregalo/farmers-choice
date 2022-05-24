from django.shortcuts import render
from .models import *
from .forms import IssueSolutionForm, IssueForm
from django.conf import settings
# Create your views here.
from user.models import User, Staff

from django.views.generic import ListView



def IndexView(request, *args, **kwargs):
    issues = Issue.objects.all()

    context = {
        'issues': issues
    }
    return render(request, 'index.html', context)

def issues(request, *args, **kwargs):
    issues = Issue.objects.all()
    form = IssueForm()

    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.farmer = request.user
            issue.save()
            form = IssueForm()
            return render(request, 'issues.html', {'form': form, 'issues': issues})

    context = {
        'issues': issues,
        'form': form
    }
    return render(request, 'issues.html', context)

def issue_detail(request, slug, *args, **kwargs):
    categories = IssueCategory.objects.all()
    issue = Issue.objects.get(slug=slug)
    issues = Issue.objects.all()[:3]
    form = IssueSolutionForm()

    issue_solutions = IssueSolution.objects.filter(issue=issue)
    print(issue_solutions)

    if request.method == 'POST' and request.user.is_authenticated:
        form = IssueSolutionForm(request.POST, request.FILES)
        if form.is_valid():
            issue_solution = form.save(commit=False)
            issue_solution.farmer = request.user
            issue_solution.issue = issue
            issue_solution.save()
            form = IssueSolutionForm()

            context = {
                'issue': issue,
                'issues': issues,
                'categories': categories,
                'issue_solutions': issue_solutions,
                'form': form
            }
            return render(request, 'issue_detail.html', context) 
    context = {
        'issue': issue,
        'issues': issues,
        'categories': categories,
        'issue_solutions': issue_solutions,
        'form': form
    }

    return render(request, 'issue_detail.html', context)


def aboutus(request, *args, **kwargs):
    experts = Staff.objects.filter(is_active=True)
    context = {
        'experts': experts
    }
    return render(request, 'about.html', context)
