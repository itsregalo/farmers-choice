from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', IndexView, name='index'),
    path('issues/', issues, name='issues'),
    path('issues/<str:slug>/', issue_detail, name='issue-detail'),
    path('about-us/', aboutus, name='about-us')
]
