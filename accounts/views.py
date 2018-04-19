from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from . import forms

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Order

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

#オーダーの一覧を表示する
def order_list(request):
    orders=Order.objects.all()
    #orders = Order.objects.filter(end_date__lte=timezone.now()).order_by('end_time')
    return render(request, 'order/order_list.html', {'orders': orders})

#オーダーの詳細を表示する
def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'order/order_detail.html', {'order': order})
