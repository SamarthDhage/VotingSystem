from django.shortcuts import render, redirect
from .forms import PartyForm
from .models import Party

def create_party(request):
    if request.method == 'POST':
        form = PartyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = PartyForm()
    return render(request, 'parties/party_form.html', {'form': form})
