from django.shortcuts import redirect, render
from . import forms

# Create your views here.
def add_author(request):
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_author')
    else:
        form = forms.AuthorForm()
    return render(request, 'add_author.html', {'form': form})