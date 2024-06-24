from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def manager_main_page(request):
    return render(request, 'mainpage_content.html')



def manager_profile(request):
    return  render(request, 'profile/index.html')

def page_not_found(request, exception):
    response = render(request, 'handler404_content.html')
    response.status_code = 404
    return response

