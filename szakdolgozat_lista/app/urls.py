from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('modositas/<int:id>/', views.szakdogaModosit, name="modositas"),
    path('torles/<int:id>', views.szakdogaTorles, name="torles")
]