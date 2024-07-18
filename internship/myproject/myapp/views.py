from django.shortcuts import render
import requests

def page1(request):
    # Make an HTTPS request
    response = requests.get('https://api.github.com')
    return render(request, 'myapp/page1.html', {'api_status': response.status_code})

def page2(request):
    # Make another HTTPS request
    response = requests.get('https://api.openweathermap.org')
    return render(request, 'myapp/page2.html', {'api_status': response.status_code})