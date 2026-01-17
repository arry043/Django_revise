from django.shortcuts import render, redirect
from .models import AlokVarity
from django.shortcuts import get_object_or_404
from .forms import AlokVarityForm
from django.contrib import messages

# Create your views here.

def all_alok(request):    
    
    aloks = AlokVarity.objects.all()
    return render(request, 'alok/all_alok.html', {'aloks':aloks})

def alok_detail(request, id):
    alok = get_object_or_404(AlokVarity, pk=id)
    return render(request, 'alok/alok_detail.html', {'alok':alok})

def add_alok_view(request):
    if request.method == 'POST':
        form = AlokVarityForm(request.POST, request.FILES)
        if form.is_valid():
            alok = form.save()
            messages.success(request, "✅ Alok added successfully!")
            return redirect('alok_detail', id=alok.id)   # ya detail page bana ho to waha bhej sakte ho
    else:
        form = AlokVarityForm()

    return render(request, 'alok/add_alok.html', {'form': form})