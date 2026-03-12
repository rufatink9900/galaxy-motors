from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')


def apps(request):
    query = request.GET.get('q', '')

    url = "https://galaxy-store-server.onrender.com/apks"
    response = requests.get(url)
    apps = response.json()

    # поиск
    if query:
        apps = [
            app for app in apps
            if query.lower() in app.get("title", "").lower()
            or query.lower() in app.get("description", "").lower()
        ]

    return render(request, "apps_list.html", {
        "apps": apps,
        "query": query
    })

@login_required(login_url='login')
def server(request):
    return render(request, 'server.html')
