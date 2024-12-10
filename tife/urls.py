from django.urls import path
from .views import main, detail, contact

urlpatterns = [
     path('', main, name="index"),
     path('detail', detail, name='more info'),
     path("contact",contact, name="contact")
]
