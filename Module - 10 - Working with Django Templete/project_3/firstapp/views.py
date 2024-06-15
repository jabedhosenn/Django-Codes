from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {'auhor' : 'Rahim', 'age':20, 'lst':[1,2,3],
         'birthday': datetime.datetime.now(), 'val': ' ', 'courses':[
        {
            'id': 1,
            'course':'django', 
            'fees':1000
            },
        {
            'id': 2,
            'course':'python', 
            'fees':2000
            },
        {
            'id': 3,
            'course':'java', 
            'fees':3000
            },
    ]}
    return render(request, 'home.html', d)