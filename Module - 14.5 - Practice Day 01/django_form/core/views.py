from django.shortcuts import render, redirect
from .forms import Info_Form, Doc_Form
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def info_form(request):
    if request.method == 'POST':
        form = Info_Form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('info_form')
    else:
        form = Info_Form()
    
    return render(request, 'core/info_form.html', {'form':form})


def doc_form(request):
    if request.method == 'POST':
        form = Doc_Form(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            profile_image = form.cleaned_data['profile_image']
            with open('uploads/files/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
                    
            with open('uploads/images/' + profile_image.name, 'wb+') as destination:
                for chunk in profile_image.chunks():
                    destination.write(chunk)
                    
            print(form.cleaned_data)
            return redirect('doc_form')
    else:
        form = Doc_Form()
    
    return render(request, 'core/doc_form.html', {'form':form})