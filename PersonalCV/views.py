from django.shortcuts import render
from django.conf import settings


def index(request):
    return render(request, str(settings.BASE_DIR) + '/templates/index.html')


def error404(request, exception):
    return render(request, str(settings.BASE_DIR) + '/templates/custom-error-pages/gear-404-page/index.html', {})


def error500(request):
    return render(request, str(settings.BASE_DIR) + '/templates/custom-error-pages/gear-500-page/index.html', {})
