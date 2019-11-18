from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats

import csv
import pandas as pd


def home(request):
    print('Home')
    return render(request, 'home.html')

def contact(request):
    print('Contact')

    return render(request, 'contact.html')

def ekspert(request):
    print('Ekspert')
    if request.method == 'POST':
        print('Form')

        bot_message = int(request.POST.get("bot_message"))
        print(bot_message)
        if bot_message <1000:
            skrypt= "<p>Za podaną kwotę, jedyne co mogę Ci polecić, to wyprawa na złom i poszukanie czegoś co jest w stanie odpalić</p> <img src=\"/static/img/500.jpg\">"
        elif bot_message >=1000 and bot_message<3000:
            skrypt= "<p>Polecany samochód, to Daewoo Lanos </p> <img src=\"/static/img/1000.jpg\">"
        elif bot_message >= 3000 and bot_message< 5000:
            skrypt= "<p> Polecany samochód, to Toyota Yaris I Generacji</p> <img src=\"/static/img/3000.png\">"
        elif bot_message >= 5000 and bot_message< 7000:
            skrypt= "<p> Polecany samochód, to Toyota Avensis I Generacji</p> <img src=\"/static/img/5000.jpg\""
        elif bot_message >=7000 and bot_message< 10000:
            skrypt= "<p>Polecany samochód, to Honda Civic VII - lata produkcji 2000-05</p> <img src=\"/static/img/7000.jpg\""
        elif bot_message >=10000 and bot_message< 15000:
            skrypt="<p>Polecany samochód, to Škoda Superb I, rocznik 2003-2005</p>  <img src=\"/static/img/10000.jpg\""
        elif bot_message>= 15000 and bot_message< 20000:
            skrypt="<p>Polecany samochód, to Toyota Celica VII 1.8 VVT-i</p>  <img src=\"/static/img/15000.jpg\""
        elif bot_message>=20000 and bot_message<30000:
            skrypt="<p>Polecany samochód, to Lexus IS II Generacja</p>  <img src=\"/static/img/20000.jpg\""
        elif bot_message >=30000 and bot_message<40000:
            skrypt="<p>Polecany samochód, to Ford Mondeo MK4</p> <img src=\"/static/img/30000.jpg\""
        elif bot_message >= 40000 and bot_message<60000:
            skrypt= "<p>Polecany samochód, to Kia Sportage III 2.0 CRDi (2010-15) </p> <img src=\"/static/img/40000.jpg\" "
        elif bot_message >= 60000 and bot_message<80000:
            skrypt= "<p>Polecany samochód, to najnowsza Toyota Corolla Seria E16 (2012-)</p> <img src=\"/static/img/60000.jpg\""
        elif bot_message >=80000 and bot_message <=100000:
            skrypt= "<p>Polecany samochód, to Audi A8 IV Generacji</p> <img src=\"/static/img/80000.jpg\" >"
        elif bot_message > 100000:
            skrypt= "<p>Masz tyle pieniędzy, że naprawdę warto kupić auto w salonie</p> <img src=\"/static/img/100000.jpg\""
        print(skrypt)
        # form = bot_message(request.POST)
        # print('\n\n' + form.data["bot_message"] + '\n\n')
        # print form.data['bot_message']
        # if form.is_valid():
        #     print form.cleaned_data['bot bot_message']
        #     print form.instane.bot_message
        return render(request, 'ekspert.html', {'result_present': True, 'skrypt': skrypt})
    return render(request, 'ekspert.html')
