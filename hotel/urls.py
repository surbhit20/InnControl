from django.urls import path

from . import views

app_name = 'hotel'

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms',views.rooms, name='rooms'),
    path('book',views.book, name='book'),
    path('thank',views.thank, name='thank'),
]