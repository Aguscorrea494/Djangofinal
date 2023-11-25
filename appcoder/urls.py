
from django.urls import path
from appcoder.views import show_html, crear_curso

urlpatterns = [
    path('show/', show_html),
    path('agregar_cursor/', crear_curso),
]
