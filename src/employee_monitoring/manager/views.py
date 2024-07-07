import datetime
from audioop import reverse

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required  # для авторизации пользователей
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginUserForm, RegisterUserForm
from .models import Booking
from .models import Address
from .models import Table
import os

REQUESTS_COUNTER = 0
counter_db = 0
started = datetime.datetime.now()


# Create your views here.


# mainpage
def manager_main_page(request):
    if request.method == 'GET':
        global REQUESTS_COUNTER
        global SEC
        REQUESTS_COUNTER += 1
        if request.user.is_authenticated:
            return HttpResponseRedirect('statistics')
        users_count = len(get_user_model().objects.all())
        seconds = (datetime.datetime.now() - started).seconds
        print(seconds)
        return render(request, '_base_mainpage.html',
                      {'users_count': users_count, 'request_counter': REQUESTS_COUNTER, 'seconds': seconds, 'counter_db': counter_db})

def manager_main_login(request):
    global REQUESTS_COUNTER
    REQUESTS_COUNTER += 1
    if request.user.is_authenticated:
        return HttpResponseRedirect('statistics')

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect('statistics')
    else:
        form = LoginUserForm()
    return render(request, 'forms/form.html', {'form': form, 'button_name': 'Вход'})


def manager_main_register(request):
    global REQUESTS_COUNTER
    global counter_db
    REQUESTS_COUNTER += 1
    if request.user.is_authenticated:
        return HttpResponseRedirect('statistics')
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            counter_db += 1
            return HttpResponseRedirect('/login')
    form = RegisterUserForm()
    return render(request, 'forms/form.html', {'form': form, 'button_name': 'Зарегистрироваться'})


@login_required(login_url='/login')
def manager_main_logout(request):
    global REQUESTS_COUNTER
    REQUESTS_COUNTER += 1

    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login')
# profile
def manager_stats(request):
    global REQUESTS_COUNTER
    REQUESTS_COUNTER += 1
    if request.method == 'POST' and request.POST.get('reservation'):  # DELETE
        print(Booking.objects.filter(pk=request.POST.get('reservation')).delete())
    return render(request, 'profile_stats.html')


@login_required(login_url='/login')
def manager_forms(request):
    global REQUESTS_COUNTER
    REQUESTS_COUNTER += 1
    if request.method == 'POST' and request.POST.get('table_number') and request.POST.get(
            'seats_available') and request.POST.get('address'):

        try:

            address = Address.objects.filter(id=int(request.POST.get('address')))
            table = Table.objects.filter(table_number=int(request.POST.get('table_number')))

            if bool(address) and bool(not (table)):
                Table(
                    table_number=request.POST.get('table_number'),
                    seats_available=request.POST.get('seats_available'),
                    status='free',
                    address=address[0]
                ).save()
                global counter_db
                counter_db += 1
        except Exception as e:
            print(e)

    elif request.method == 'POST' and request.POST.get('delete_table'):
        try:
            Table.objects.filter(table_number=int(request.POST.get('delete_table'))).delete()
        except Exception as e:
            print(e)

    return render(request, 'profile_addtable.html')


@login_required(login_url='/login')
def manager_address(request):
    global REQUESTS_COUNTER
    REQUESTS_COUNTER += 1
    try:
        if request.method == 'POST' and request.POST.get('address'):  # add address
            Address(location=f"{request.POST.get('address')}").save()
            global counter_db
            counter_db += 1

        if request.method == 'POST' and request.POST.get('del_address'):  # add address
            Address.objects.filter(id=int(f"{request.POST.get('del_address')}")).delete()
    except Exception as e:
        print(e)
    return render(request, 'profile_addaddress.html')


def reservation(request):
    global REQUESTS_COUNTER
    REQUESTS_COUNTER += 1
    if request.method == 'GET' and request.GET.get('id'):
        print('test')
        tables = Table.objects.filter(address=request.GET.get('id'))
        if tables:
            return render(request, 'reservation.html', context={'tables': tables})
        else:
            return render(request, 'reservation.html', context={'tables': '0'})
    elif request.method == 'POST' and request.POST.get('booking_date') and request.POST.get(
            'comment') and request.POST.get('number_of_people') and request.POST.get('tables'):
        print('test')
        Booking(
            booking_date=request.POST.get('booking_date'),
            comment=request.POST.get('comment'),
            number_of_people=request.POST.get('number_of_people'),
            table=Table.objects.filter(table_number=request.POST.get('tables'))[0]
        ).save()
        global counter_db
        counter_db += 1

        tables = Table.objects.filter(address=request.GET.get('id'))

        if tables:
            return render(request, 'reservation.html', context={'tables': tables})
        else:
            return render(request, 'reservation.html', context={'tables': '0'})

    tables = Table.objects.filter(address=request.GET.get('id'))
    if tables:
        return render(request, 'reservation.html', context={'tables': tables})
    else:
        return render(request, 'reservation.html', context={'tables': '0'})
