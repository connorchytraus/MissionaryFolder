from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def indexPageView(request) :
    return render(request, 'homepages/index.html')

def journalPageView(request) :
    return render(request, 'homepages/journal.html')