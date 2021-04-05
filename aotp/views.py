from django.shortcuts import render
from django.views.generic import TemplateView

import requests
import sys
from subprocess import run, PIPE
from . import functions

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

def external(request):
    img_data = request.POST.get('img_data')
    out = functions.post_img(img_data)
    # out = run([sys.executable, '//aotp//functions.py', img_data], shell=False, stdout=PIPE)
    # print(out)
    return render(request, 'home.html',{'data1':out})

