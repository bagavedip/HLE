from django.shortcuts import render
import json
import requests
from . form import ActionForm


def index(request):
    url = ActionForm()
    return render(request, 'index.html', {'form': url})


def convert(request):
    if request.method == "GET":
        title = request.GET.get('url')
        print(title)
        response = requests.get(title)
        packages_json = response.json()
        return render(request, 'convert.html', {'resp': packages_json})
