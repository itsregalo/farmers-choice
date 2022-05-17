from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Issue)
admin.site.register(IssueSolution)
admin.site.register(IssueCategory)
admin.site.register(Farmer)
admin.site.register(IssueVote)
admin.site.register(IssueSolutionVote)
