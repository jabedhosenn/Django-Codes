from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.(cookie)
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'Rahul', max_age=10)
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    return render(request, 'get_cookie.html', {'name': name})

def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')
    return response

# Django Session
# Session vs Cookie

def set_session(request):
    data = {
        'name' : 'Rahul',
        'age' : 23,
        'language' : 'Bangla'
    }
    request.session.update(data)
    return render(request, 'set_session.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session['name']
        age = request.session['age']
        language = request.session['language']
        request.session.modified = True
        return render(request, 'get_session.html', {'name': name, 'age': age,
                                                    'language': language})
    else:
        return HttpResponse("Session Expired")
        

def delete_session(request):
    # del request.session['name']
    request.session.clear()
    request.session.flush()
    return render(request, 'delete_session.html')
