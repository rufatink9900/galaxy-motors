# views.py
from django.shortcuts import render, get_object_or_404
from .models import App
from django.http import HttpResponse


def apps_list(request):
    apps = App.objects.all().order_by('-id')
    return render(request, 'apps_list.html', {'apps': apps})

def app_detail(request, pk):
    app = get_object_or_404(App, pk=pk)
    return render(request, 'app_detail.html', {'app': app})



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

