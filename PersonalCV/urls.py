from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    url('admin/', admin.site.urls),
    path('', views.index, name='Home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)