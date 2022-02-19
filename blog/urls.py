from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="starting-page"),
    path("", views.StartingPostListView.as_view(), name="blog-starting-page"),
    path("posts/", views.AllPostListView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post-detail-page")
]