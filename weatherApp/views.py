from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json
# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        city = city.replace(" ", "+")
        source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=89bbb854e6458db73b36c1e83a467a23').read()
        data_list = json.loads(source)
        if data_list["cod"] == 200:
            data = {
                "place": f"{data_list['name']}, {data_list['sys']['country']}",
                "temperature": f"{data_list['main']['temp']}°C",
                "pressure": str(data_list['main']['pressure']),
                "humidity": str(data_list['main']['humidity']),
                "feels_like": f"{data_list['main']['feels_like']}°C",
                "description": str(data_list['weather'][0]['description']),
                "icon": data_list['weather'][0]['icon'],
                "cod": data_list['cod'],
            }
        else:
            data={
                "cod": data_list['cod']
            }
    else: 
        data = {}
    return render(request, 'weatherApp/index.html', data)
