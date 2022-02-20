from .models import Post
from .forms import CommentForm
from django.views.generic import ListView
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


SESSION_STORED_POSTS_ID = "stored_id"


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

        context = self.create_context(request, post, CommentForm())

        return render(request, self.template_name, context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = get_object_or_404(Post, slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = self.create_context(request, post, comment_form)
        return render(request, self.template_name, context)

    def create_context(self, request, post, comment_form):
        stored_posts = request.session.get(SESSION_STORED_POSTS_ID)
        if stored_posts is None or len(stored_posts) == 0:
            is_saved_for_later = False
        else:
            is_saved_for_later = post.id in stored_posts

        context = {
            self.context_object_name: post,
            "tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "is_saved_for_later": is_saved_for_later
        }
        return context


class ReadLaterView(View):
    def get(self, request):
        stored_post = request.session.get(SESSION_STORED_POSTS_ID)
        context = {}
        if stored_post is None or len(stored_post) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_post)
            context["posts"] = posts
            context["has_posts"] = len(posts) > 0

        return render(request, "blog/read-later-posts.html", context)

    def post(self, request):
        stored_post = request.session.get(SESSION_STORED_POSTS_ID)
        if stored_post is None:
            stored_post = []
        post_id = int(request.POST["post_id"])
        if post_id not in stored_post:
            stored_post.append(post_id)
        else:
            stored_post.remove(post_id)

        request.session[SESSION_STORED_POSTS_ID] = stored_post

        return HttpResponseRedirect("/")
