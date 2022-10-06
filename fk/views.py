from django.shortcuts import render
from fk.views import render
# Create your views here.
def index(request):
    return render (request , 'fk.html')