from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("review", views.ReviewView.as_view(), name="review"),
    path("thank-you", views.thank_you, name="thank-you"),
    path("<slug:slug>", views.book_detail, name="book_detail")
]