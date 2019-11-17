from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats

import csv
import pandas as pd


def home(request):
    print('Home')
    return render(request, 'home.html')


def about(request):
    print('About')
    return render(request, 'about.html')


def contact(request):
    print('Contact')

    return render(request, 'contact.html')

def ekspert(request):
    print('Ekspert')
    if request.method == 'POST':
        print('Form')

        bot_message = request.POST.get("bot_message")
        print(bot_message)
        if bot_message == '3000':
            skrypt= "<p> Polecany samochód,to Toyota Yaris I Generacji</p> <img src=\"/static/img/3000.png\" >"
        if bot_message == '5000':
            skrypt= "<p> Polecany samochód,to Toyota Avensis I Generacji</p> <img src=\"/static/img/5000.jpg\" > "
        print(skrypt)
        # form = bot_message(request.POST)
        # print('\n\n' + form.data["bot_message"] + '\n\n')
        # print form.data['bot_message']
        # if form.is_valid():
        #     print form.cleaned_data['bot bot_message']
        #     print form.instane.bot_message
        return render(request, 'ekspert.html', {'result_present': True, 'skrypt': skrypt})
    return render(request, 'ekspert.html')
