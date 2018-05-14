from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from . import forms
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Order
from .models import Station
from django.contrib.auth import views as auth_views


import socket
import binascii
from datetime import datetime
from time import sleep

@login_required
#indexページを表示する動作はここで記述する
def index(request):
    station_id=request.session['station_id']
    print("index_test  "+ str(station_id))
    return render(request, 'accounts/index.html', {'station_id':station_id})

#ログインページ表示するときの処理
def login(request, template_name):
    #print("login_test0  " + str(request.session['station_id']))
    # if 'station_id' not in request.session or 'station_id'== None:
    if request.GET.get(key="station_id") is not None:
        request.session['station_id'] = request.GET.get(key="station_id")
            #'station_id': request.GET.get(key="station_id", default="hogehoge")
        print("login_test " + str(request.session['station_id']))
    #標準ログイン処理を呼び出す
    return auth_views.login(request, template_name=template_name)

#ユーザー新規作成フォームを提示する
def new(request):
#    form=UserCreationForm()
    form = forms.UserCreateForm()
    return render(request, 'accounts/new.html', {'form': form,})

#ユーザーを作成する
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



#オーダーを作成する
def create_order(request):
    if request.method == 'POST':
        #各種類の電子決済APIを呼び出し、デポジット処理を行う
        #バッテリを吐き出す処理をする

        s = socket.socket()
        port = 8100
        s.bind(('', port))
        print('listening')
        s.listen(5)
        c, addr = s.accept()
        #print('receiving')
        #print(binascii.hexlify(c.recv(4096)))
        print('sending')
        # Wifi
        borrow = binascii.a2b_hex("55AA1202110a000058FF01525AA5")
        # 4G
        # borrow = binascii.a2b_hex("55AA1202110a00008fFF01855AA5")
        c.send(borrow)
        c.close()
        s.close()
        # バッテリIDはステーションからの戻り値を取得
        #オーダーID,ステーションID,バッテリID,現在時間、ユーザーIDなどの情報を記録する
        #オーダーIDは自動採番,ユーザーIDとステーションIDはセッションから取得

        print(int(request.session['station_id']))
        a = Order(user_id=User.objects.get(id=1), station_id_borrow=Station.objects.get(id=int(request.session['station_id'])))
        #a = Order(user_id=User.objects.get(id=1), station_id_borrow=Station.objects.get(id=3))
        a.save()  # INSERTが実行される
        return render(request, 'accounts/rental_success.html')
    else:
        raise Http404

#ユーザー新規作成フォームを提示する
def return_to_indexpage(request):
    return render(request, 'accounts/index.html')

#オーダーの一覧を表示する
def order_list(request):
    orders=Order.objects.all()
    #orders = Order.objects.filter(end_date__lte=timezone.now()).order_by('end_time')
    return render(request, 'order/order_list.html', {'orders': orders})

#オーダーの詳細を表示する
def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    print (id)
    return render(request, 'order/order_detail.html', {'order': order})
