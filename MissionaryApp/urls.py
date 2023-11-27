from django.urls import path
from .views import indexPageView
from .views import journalPageView

urlpatterns = [
    path('', indexPageView, name="home"),
    path('journal/', journalPageView, name='journal'),
]
