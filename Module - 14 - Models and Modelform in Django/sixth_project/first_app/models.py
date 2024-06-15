from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    address = models.TextField()
    father_name = models.TextField(default='Name')

    def __str__(self):
        return f"ID: {self.id} - {self.name}"