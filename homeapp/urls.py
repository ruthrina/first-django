from django.urls import path

from .views import homePageView
from .views import aboutPageView
from .views import contactPageView

urlpatterns = [
    path('', homePageView, name='homepage'),
    path('about', aboutPageView, name='aboutpage'),
    path('contact', contactPageView, name='contactpage')
]