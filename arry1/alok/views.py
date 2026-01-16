from django.shortcuts import render
from .models import AlokVarity
from django.shortcuts import get_object_or_404

# Create your views here.

def all_alok(request):    
    
    aloks = AlokVarity.objects.all()
    return render(request, 'alok/all_alok.html', {'aloks':aloks})

def alok_detail(request, id):
    alok = get_object_or_404(AlokVarity, pk=id)
    return render(request, 'alok/alok_detail.html', {'alok':alok})

