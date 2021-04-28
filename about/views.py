from django.shortcuts import render
import requests
# Create your views here.


def aboutView(req):
    data = [1, 2, 3, 4, 5]
    return render(req, "about/about.html", {"data": data})
