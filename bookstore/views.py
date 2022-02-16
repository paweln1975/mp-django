from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg, Min, Max
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.views import View


def index(request):
    books = Book.objects.all().order_by("-rating")
    number_of_books = books.count
    avg_rating = books.aggregate(Avg("rating"), Min("rating"), Max("rating"))
    return render(request, "bookstore/index.html", {
        "books": books,
        "number_of_books": number_of_books,
        "avg_rating": avg_rating
    })


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)

    return render(request, "bookstore/book_detail.html", {
        "book": book
    })


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "bookstore/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/bookstore/thank-you")
        return render(request, "bookstore/review.html", {
            "form": form
        })


def thank_you(request):
    return render(request, "bookstore/thank_you.html")

