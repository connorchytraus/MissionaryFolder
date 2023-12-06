from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Goal  # Import your Goal model


def add_goal_view(request):
    if request.method == "POST":
        goal_text = request.POST.get("goal")

        # Assuming you have a Goal model with a 'text' field
        new_goal = Goal.objects.create(text=goal_text)

        # Optionally, you can redirect the user to a different page
        return redirect("your_redirect_url")

    return HttpResponse("Invalid Request")


# Create your views here.
def indexPageView(request):
    return render(request, "homepages/index.html")


def journalPageView(request):
    return render(request, "homepages/journal.html")


def goalsPageView(request):
    return render(request, "homepages/goals.html")


def setGoal(request):
    return render(request, "homepages/setGoal.html")

def resourcesPageView(request):
        return render(request, "homepages/resources.html")
