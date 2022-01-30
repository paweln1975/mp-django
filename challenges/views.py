from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
challenges = {
    "january": "Walk for 20 minutes per day",
    "february": "Read for 5 minutes per day",
    "march": "Learn Django for 10 minutes per day",
    "april": "Pray for 3 minutes per day",
    "may": "Default may challenge",
    "june": "Default june challenge",
    "july": "Default july challenge",
    "august": "Default august challenge",
    "september": "Default september challenge",
    "october": "Default october challenge",
    "november": None,
    "december": None,

}


def index(request):
    list_items = ""
    months = list(challenges.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month}</a></li>"

    return render(request, "challenges/index.html", {
        "months": months
    })


def month_challenge(request, month):
    try:
        challenge = challenges[month]
        response = render(request, "challenges/challenge.html", {
            'month': month,
            'text': challenge
        })
        return response
    except KeyError:
        raise Http404()


def month_challenge_by_number(request, month):
    months = list(challenges.keys())
    if month <= len(months):
        redirect_path = reverse("month-challenge", args=[months[month-1]])
        return HttpResponseRedirect(redirect_path)
    else:
        raise Http404()


def template_loader(request):
    return render(request, template_name="challenges/index.html")

