from django.shortcuts import render
from django.views.generic import TemplateView

import requests
import sys
from subprocess import run, PIPE
from . import functions

from rq import Queue
from . import worker

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

def external(request):
    img_data = request.POST.get('img_data')
    artist = request.POST.get('artist')
    title = request.POST.get('title')
    q.enqueue(functions.post_img, ttl=120, args=(img_data, artist, title))
    # functions.post_img_temp(img_data, artist, title)
    return render(request, 'home.html')

q = Queue(connection = worker.conn)