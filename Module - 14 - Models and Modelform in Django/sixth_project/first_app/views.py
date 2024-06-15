from django.shortcuts import render, redirect
from . import models
# Create your views here.
def home(request):
    student = models.Student.objects.all()
    return render(request, 'home.html', {'data': student})

def delete_student(request, id):
    # student = models.Student.objects.get(id=id)
    # student.delete()
    # models.Student.objects.filter(id=id).delete()
    std = models.Student.objects.get(pk=id).delete()
    return redirect("homepage")