from django.shortcuts import render, get_object_or_404
from .models import Book, Review, Profile
from django.db.models import Avg, Min, Max
from .forms import ReviewForm, ProfileForm
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.http import HttpResponseRedirect


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


class ReviewCreateView(CreateView):
    model = Review
    template_name = "bookstore/review.html"
    form_class = ReviewForm
    success_url = "thank-you"


class ReviewUpdateView(UpdateView):
    model = Review
    template_name = "bookstore/review.html"
    form_class = ReviewForm

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("review-detail", kwargs={"pk": pk})


class ReviewListView(ListView):
    template_name = "bookstore/review_list.html"
    model = Review
    paginate_by = 5
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(id__gt=0).order_by("id")
        print(data.query)
        return data


class ReviewDetailView(DetailView):
    template_name = "bookstore/review_detail.html"
    model = Review
    context_object_name = "review"


class ThankYouView(TemplateView):
    template_name = "bookstore/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "bookstore/create_profile.html", {
            "form": form
        })

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            profile = Profile(image=request.FILES["user_image"], file_name=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("thank-you")

        return render(request, "bookstore/create_profile.html"), {
            "form": submitted_form
        }


class CreateProfileViewBased(CreateView):
    template_name = "bookstore/create_profile.html"
    model = Profile
    fields = ["image"]
    success_url = "thank-you"


class ProfilesView(ListView):
    template_name = "bookstore/profiles.html"
    model = Profile
    context_object_name = "profiles"
