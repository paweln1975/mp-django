from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("review", views.ReviewCreateView.as_view(), name="review-create"),
    path("reviews", views.ReviewListView.as_view(), name="reviews"),
    path("review/<int:pk>/update", views.ReviewUpdateView.as_view(), name="review-update"),
    path("review/<int:pk>", views.ReviewDetailView.as_view(), name="review-detail"),
    path("thank-you", views.ThankYouView.as_view(), name="thank-you"),
    path("profile", views.CreateProfileView.as_view(), name="profile-create"),
    path("profile-new", views.CreateProfileViewBased.as_view(), name="profile-create"),
    path("book/<slug:slug>", views.book_detail, name="book_detail"),
    path("profiles", views.ProfilesView.as_view(), name="profile-list"),
]


