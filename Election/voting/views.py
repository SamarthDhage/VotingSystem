from django.shortcuts import render,redirect
from Parties.models import Party
from .models import Vote
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    context = { 
        'parties' : Party.objects.all()
    }    
    return render(request, 'voting/home.html', context)


@login_required
def vote(request):
    user_vote = Vote.objects.filter(user=request.user).first()
    if request.method == 'POST':
        if user_vote:
            messages.error(request, 'You have already voted.')
            return redirect('vote')

        party_id = request.POST.get('party_id')
        if party_id:
            try:
                party = Party.objects.get(id=party_id)
                Vote.objects.create(user=request.user, party=party)
                party.votes += 1
                party.save()
                messages.success(request, 'Your vote has been recorded.')
            except Party.DoesNotExist:
                messages.error(request, 'Invalid party selected.')
        return redirect('vote')

    context = { 
        'parties': Party.objects.all(),
        'user_vote': user_vote
    }
    return render(request, 'voting/vote.html', context)

@login_required
def results(request):
    if not request.user.is_superuser:
        messages.warning(request, 'You do not have permission to check the results NOW!!!')
        return redirect('home')
    else:
        parties = Party.objects.all()
        context = {
            'parties': parties
        }
        return render(request, 'voting/results.html', context)