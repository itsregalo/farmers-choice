from django.db import models
from django.utils.text import slugify
# import settings
from django.conf import settings

# imagekit is a library for resizing an image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

User = settings.AUTH_USER_MODEL

# Create your models here.

# farmer class
class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    is_largescale = models.BooleanField(default=False)

    # __str__ method to return username for the user
    def __str__(self):
        return self.user.username

    # method to count the number of farmers
    def count_farmers():
        return Farmer.objects.count()

# issue category class
class IssueCategory(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save()
        

    class Meta:
        verbose_name_plural = 'issue Categories'

    # __str__ method to return username for the user
    def __str__(self):
        return self.name

    # method to count the number of issue categories
    def count_issue_categories():
        return IssueCategory.objects.count()

    # a method to get all the issues in a category
    def get_category_issues(self):
        return Issue.objects.filter(category=self)

# issue class
class Issue(models.Model):
    category = models.ForeignKey(IssueCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/issues/', blank=True)
    pic_thumbnail = ImageSpecField(source='image',
                                   processors = [ResizeToFill(494, 326)],
                                   format='JPEG',
                                   options = {'quality':100})
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100, blank=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, null=True)

    # this is a method used to create the field slug when the issue is created
    # slug is a unique field that is used to create a url for the issue
    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save()

    # __str__ method to return username for the user
    def __str__(self):
        return self.title

    # method to count the number of issues
    def count_issues():
        return Issue.objects.count()

    # method to delete the issue
    def delete_issue(self):
        self.delete()

# issue vote class
class IssueVote(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    voter = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    # __str__ method to return username for the user
    def __str__(self):
        return self.voter.user.username

# issue solution class
class IssueSolution(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    votes = models.IntegerField(default=0)

    # __str__ method to return username for the user
    def __str__(self):
        return self.farmer.user.username

# issue solution vote class
class IssueSolutionVote(models.Model):
    solution = models.ForeignKey(IssueSolution, on_delete=models.CASCADE)
    voter = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    # __str__ method to return username for the user who voted
    def __str__(self):
        return self.voter.user.username
