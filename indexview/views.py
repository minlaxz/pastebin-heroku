from django.shortcuts import render
import requests
# Create your views here.


def indexView(req):
    res = requests.get("https://minlaxz-bundle.firebaseio.com/public-notes.json")
    data = res.json().values()
    # data = [1, 2, 3, 4, 5]
    return render(req, "indexview/index.html", {"data": data})
