from django.shortcuts import render_to_response
from django.shortcuts import render

def ana_sayfa(request):
    return render_to_response('home.html',locals())