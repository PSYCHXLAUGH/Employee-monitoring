from django.contrib.auth.decorators import login_required  # для авторизации пользователей
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Booking
from .models import Address
from .models import Table


# Create your views here.


# mainpage
def manager_main_page(request):
    return render(request, 'mainpage_content.html')


def manager_main_login(request):
    return render(request, 'mainpage_login.html')


def manager_main_register(request):
    return render(request, 'mainpage_register.html')


# profile
def manager_stats(request):
    if request.method == 'POST' and request.POST.get('reservation'):  # DELETE
        print(Booking.objects.filter(pk=request.POST.get('reservation')).delete())
    return render(request, 'profile_stats.html')


@login_required
def manager_forms(request):
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
        except Exception as e:
            print(e)

    elif request.method == 'POST' and request.POST.get('delete_table'):
        try:
            Table.objects.filter(table_number=int(request.POST.get('delete_table'))).delete()
        except Exception as e:
            print(e)

    return render(request, 'profile_addtable.html')


@login_required
def manager_address(request):
    try:
        if request.method == 'POST' and request.POST.get('address'):  # add address
            Address(location=f"{request.POST.get('address')}").save()

        if request.method == 'POST' and request.POST.get('del_address'):  # add address
            Address.objects.filter(id=int(f"{request.POST.get('del_address')}")).delete()
    except Exception as e:
        print(e)
    return render(request, 'profile_addaddress.html')


def manager_links(request):
    return render(request, 'profile_getlinks.html')


@login_required
def reservation(request):
    # Booking(booking_date=datetime.datetime.now(), comment='helloasefworld', number_of_people=10,
    #         table=Table.objects.all()[0]).save()

    if request.method == 'GET' and request.GET.get('id'):
        print('test')
        tables = Table.objects.filter(address=request.GET.get('id'))
        if tables:
            return render(request, 'reservation.html', context={'tables': tables})
        else:
            return render(request, 'reservation.html', context={'tables': '0'})


    elif request.method == 'POST' and request.POST.get('booking_date') and request.POST.get('comment') and request.POST.get('number_of_people') and request.POST.get('tables'):
        print('test')
        Booking(
            booking_date=request.POST.get('booking_date'),
            comment=request.POST.get('comment'),
            number_of_people=request.POST.get('number_of_people'),
            table=Table.objects.filter(table_number=request.POST.get('tables'))[0]
        ).save()

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