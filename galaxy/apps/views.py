# views.py
from django.shortcuts import render, get_object_or_404
from .models import App
from django.db.models import Q
from django.http import HttpResponse


def apps_list(request):
    query = request.GET.get('q', '')  # текст поиска

    apps = App.objects.all()

    if query:
        apps = apps.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    apps = apps.order_by('-id')

    return render(request, 'apps_list.html', {
        'apps': apps,
        'query': query
    })


def app_detail(request, pk):
    app = get_object_or_404(App, pk=pk)
    related_apps = App.objects.exclude(pk=pk).order_by('-created_at')[:4]
    return render(request, 'app_detail.html', {
        'app': app,
        'related_apps': related_apps
    })


def download_apk(request, app_id):
    app = get_object_or_404(App, id=app_id)
    if not app.apk_file:
        return HttpResponse("File not found", status=404)

    response = HttpResponse(
        app.apk_file,
        content_type='application/vnd.android.package-archive'
    )
    response['Content-Disposition'] = f'attachment; filename="{app.apk_filename}"'
    return response


def q07(request):
    return render(request, 'q07.html')