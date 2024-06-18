from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category) # ekta post multiple category er moddhe thakte pare abar ekta category er moddhe multiple post thakte pare
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/media/uploads/', blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comment')
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #jpkhon ei class er objwct made hobe shei time bole dibe
    updated_at = models.DateTimeField(auto_now=True) #jpkhon ei class er objwct
    def __str__(self) -> str:
        return f"Comments by {self.name}"