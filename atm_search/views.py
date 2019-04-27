from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from data.atms import get_locations
import string

# with open('C:/Users/MD SUMON/Desktop/ATM_Search/atm_search/templates/index.html') as f:
# template2 = Template(f.read())
# template = Template('<h1 style="color:red;font-style:bold">{{msg}}</h1>')


def index(request: HttpRequest):
    search_query = request.GET.get('search')
    search_query = search_query.capwords()
    if search_query:
        atm_list = filter(lambda atm: search_query in atm.location, get_locations())
    else:
        atm_list = get_locations()
    context = {"atm": atm_list}
    return render(request, 'index.html', context)
