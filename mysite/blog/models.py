from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

# Creating a customize manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'), 
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish') # Unique for date prevents two posts from having the same slug for a given date
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # Many to one relationship
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True) # Auto now add save the date when created
    updated = models.DateTimeField(auto_now=True) # Auto now update the date automatically when saved
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    class Meta:
        ordering = ('-publish',) # Sort results by the publish field in descending order
                
    def __str__(self):
        return self.title
    
    # If we declare any manager for the model but we want to keep the objects manager,
    # we have to add it explicitly to our model.
    objects = models.Manager() # The default manager. 
    published = PublishedManager() # Our custom manager


