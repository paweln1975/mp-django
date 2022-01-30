from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("months", views.template_loader),
    path("<int:month>", views.month_challenge_by_number),
    path("<str:month>", views.month_challenge, name="month-challenge"),
]
