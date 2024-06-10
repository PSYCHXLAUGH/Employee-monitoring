from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse('test')


def table_list(request, table_id):

    if int(table_id) > 5:
        return redirect('/')
    return HttpResponse(str(table_id))

def page_not_found(request, exception):
    return HttpResponseNotFound("not found")