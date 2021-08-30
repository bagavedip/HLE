from django.shortcuts import render
import requests
from . form import ActionForm
import pandas as pd
import pandasvalidation as pv
import datetime
from validate_email import validate_email
import numpy as np
import re


def index(request):
    url = ActionForm()
    return render(request, 'index.html', {'form': url})


def convert(request):
    if request.method == "GET":
        title = request.GET.get('url')
        r = requests.get(title)
        res = pd.read_excel(title)
        df = pd.DataFrame(res)
    return render(request, 'convert.html', {'resp': df})



