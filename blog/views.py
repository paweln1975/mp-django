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
        context = self.create_context(post, CommentForm())

        return render(request, self.template_name, context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = get_object_or_404(Post, slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = self.create_context(post, comment_form)
        return render(request, self.template_name, context)

    def create_context(self, post, comment_form):
        context = {
            self.context_object_name: post,
            "tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id")
        }
        return context


class ReadLaterView(View):
    def post(self, request):
        stored_post = request.session.get("stored_id")
        if stored_post is None:
            stored_post = []
        post_id = int(request.POST["post_id"])
        if post_id not in stored_post:
            stored_post.append(post_id)

        return HttpResponseRedirect("/")
