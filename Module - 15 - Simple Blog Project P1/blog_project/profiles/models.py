from django.db import models
from author.models import Author

# Create your models here.
class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_picture = models.ImageField(upload_to='profile_pictures', default='default.jpg')
    # bio = models.TextField(max_length=500, blank=True)

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    about = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.name
