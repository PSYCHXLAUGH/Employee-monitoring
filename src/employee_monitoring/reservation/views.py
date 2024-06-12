from django.http import HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.template.loader import render_to_string
from django.urls import reverse


# Create your views here.


def reservation_mainpage(request):
    return HttpResponse('main_page')

def reservation_table(request, table_id):
    if table_id > 10:
        raise Http404()
    elif table_id == 1:
        return redirect(to='/') # GET /1 HTTP/1.1 302 0
    elif table_id == 2:
        uri = reverse('reservation_table', args=(4,))
        return redirect(uri)
    elif table_id == 5:
        return HttpResponseRedirect('/')
    elif table_id == 6:
        return render(request, 'reservation_templates/auth.html')
    return HttpResponse(f'reservation {table_id}')

def page_not_found(request, exception):
    return HttpResponseNotFound("not found")