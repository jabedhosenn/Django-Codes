from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('info_form/', views.info_form, name='info_form'),
    path('doc_form/', views.doc_form, name='doc_form'),
]