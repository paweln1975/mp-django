from .models import Post
from .forms import CommentForm
from django.views.generic import ListView
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def get_date(post):
    return post["date"]


class StartingPostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/index.html"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by("-post_date")[:3]
        return data


class AllPostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/all-posts.html"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by("-post_date")
        return data


class PostDetailView(View):
    template_name = "blog/post-detail.html"
    model = Post
    context_object_name = "post"

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        context = {
            self.context_object_name: post,
            "tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all()
        }
        return render(request, self.template_name, context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = get_object_or_404(Post, slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            self.context_object_name: post,
            "tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all()
        }
        return render(request, self.template_name, context)


