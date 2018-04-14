from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from . import forms

@login_required
def index(request):
    return render(request, 'accounts/index.html')

def new(request):
#    form=UserCreationForm()
    form = forms.UserCreateForm()
    return render(request, 'accounts/new.html', {'form': form,})

def create(request):
    if request.method == 'POST':
#        form = UserCreationForm(request.POST)]
        form = forms.UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./login')
        return render(request, 'accounts/new.html', {'form': form,})
    else:
        raise Http404


