from django.shortcuts import render
from django.views.generic import TemplateView

import requests
import sys
from subprocess import run, PIPE
from . import functions

class HomePageView(TemplateView):
    template_name = "home.html"

def external(request):
    img_data = request.POST.get('img_data')
    artist = request.POST.get('artist')
    title = request.POST.get('title')
    functions.post_img(img_data, title, artist)
    return render(request, 'home.html')