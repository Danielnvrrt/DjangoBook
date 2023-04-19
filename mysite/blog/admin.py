from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin): # Registering the model using a custom class that inherits from ModelAdmin
    list_display = ('title', 'slug', 'author', 'publish', 'status') # How the information is gonna be displayed
    list_filter = ('status', 'created', 'publish', 'author') # Right sidebar to filter by these fields included
    search_fields = ('title', 'body') # Searchable fields in the search bar
    prepopulated_fields = {'slug': ('title',)} # When adding a new post, as you type the title, the slug field is filled 
    raw_id_fields = ('author',) # Lookup widget for the author when adding a new post
    date_hierarchy = 'publish' # Navigation links to navigate through a date hierarchy
    ordering = ('status', 'publish') # Ordered by