from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def manager_main_page(request):
    return render(request, 'mainpage_content.html')
