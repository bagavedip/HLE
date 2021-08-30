import pandas as pd
from django.shortcuts import render, redirect
# from django.conf import settings
from django.core.files.storage import FileSystemStorage
# import openpyxl
from . form import ActionForm
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import os


def home(request):
    try:
        if request.method == 'POST':
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            file_path = settings.MEDIA_ROOT + '/' + myfile.name
            path = os.path.join(fs.location + '/' + myfile.name)
            # print(path)
            df_json = pd.read_excel(str(path))
            df = pd.DataFrame(df_json)
            result = df.loc[:, ['Id', 'Name', 'Phone', 'Email', 'City', 'BHK Configuration', 'Expected Rent', 'TNC Acceptance', 'Comments', 'Date']]
            a = result.isnull().sum()
            return render(request, 'converts.html', {'df': a})

        else:
            file = ActionForm()
        return render(request, 'home.html', {'file': file})
    except BaseException as e:
        print(str(e))
