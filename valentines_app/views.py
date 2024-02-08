from django.shortcuts import render, redirect
from .models import ValentineCard
from .forms import ValentineCardForm

def home(request):
    cards = ValentineCard.objects.all()
    return render(request, 'valentines_app/home.html', {'cards': cards})

def send_card(request):
    if request.method == 'POST':
        form = ValentineCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ValentineCardForm()
    return render(request, 'valentines_app/send_card.html', {'form': form})
