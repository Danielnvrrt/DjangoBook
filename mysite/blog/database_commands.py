from django.contrib.auth.models import User
from .models import Post

# Create objects
user = User.objects.get(username='usuario') # Retrieve user
post = Post(title='Another Post', slug='another-post', body='Post body.', author=user) # Create new Post
post.save() # Perform an INSERT SQL statement

# Create and insert in a single operation
Post.objects.create(title='One more post', slug='one-more-post', body='Post body.', author=user)

# Update objects
post.title = 'New title'
post.save() # This time performs an UPDATE SQL statement

# Retrieving objects
all_posts = Post.objects.all() # Retrieve all objects. 
# This last QuerySet is not executed because Django QuerySets are lazy, which means they are only evaluated
# when they are forced to be, making QuerySets very efficient

# Filter QuerySet
Post.objects.filter(publish__year=2023) # Retrieve all posts published in 2023
Post.objects.filter(publish__year=2023, author__username='usuario') # Retrieve all posts published in 2023 by the author...

# Excluding Results
Post.objects.filter(publish__year=2023).exclude(title__startswith='1') # Retrieve all posts published in 2023 whose titles don't start with 1

# Order by Results
Post.objects.order_by('title') # Retrieve all objects ordered by their title. Ascending order is implied.
Post.objects.order_by('-title') # Descending order with a negative sign prefix

# Delete objects
post = Post.objects.get(id=1)
post.delete()

# Using custom manager published
Post.published.all()