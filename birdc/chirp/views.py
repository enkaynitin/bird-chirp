from django.shortcuts import render
from .models import Chirp
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.db.models import Q
from .forms import SearchForm, ChirpForm
from .models import Chirp
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required
def index(request):
    if request.method == 'POST':
        cform = ChirpForm(request.POST)
        if cform.is_valid():
            chirp = cform.save()
            return HttpResponseRedirect('chirp/')
    else:
        cform = ChirpForm()

    return render(request, 'chirp/chirp.html', {'cform':cform})

@csrf_exempt
def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )
        results = User.objects.filter(qset).distinct()
    else:
        results = []
    return render(request, 'chirp/search_user.html', {
        "results": results,
        "query": query
    })



def follow(request, user_id):
    pass


def find_user_by_name(query_name):
   result = User.objects.filter(first_name__startswith=query_name)
   return result





def show_chirps(request):
    pass





