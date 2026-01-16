from django.shortcuts import render
from .models import AlokVarity

# Create your views here.

def all_alok(request):    
    
    aloks = AlokVarity.objects.all()
    return render(request, 'alok/all_alok.html', {'aloks':aloks})