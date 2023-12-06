from django.urls import path
from .views import indexPageView
from .views import journalPageView
from .views import goalsPageView

urlpatterns = [
    path("", indexPageView, name="home"),
    path("journal/", journalPageView, name="journal"),
    path("goals/", goalsPageView, name="goals"),
]
