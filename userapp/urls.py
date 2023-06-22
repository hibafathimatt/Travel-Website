from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',views.home),
    path('login',views.login),
    path('index',views.index),
    path('reg',views.reg),
    path('details',views.details),
    path('edit',views.edit),
    path('update',views.update),
    path('delete',views.delete),
    path('upload',views.upload),
    path('traview',views.traview),
    path('destination',views.destination),
    path('hampi',views.hampi),
    path('book',views.book),
    path('contact',views.contact),
    path('about',views.about),
    path('hampii',views.hampii),
    path('custom',views.custom),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
