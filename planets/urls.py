from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

if settings.DEBUG:
    urlpatterns = [
        path('', views.planet_detail, name='planet_detail'),
        path('<str:slug>/', views.planet_detail, name='planet_detail'),
        path(
            '<str:slug>/structure',
            views.planet_detail,
            name='planet_structure'
        ),
        path(
            '<str:slug>/geology',
            views.planet_detail,
            name='planet_geology'
        ),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
