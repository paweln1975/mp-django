from django.shortcuts import render, get_object_or_404
from .models import Post


def get_date(post):
    return post["date"]


def index(request):
    last_3_posts = Post.objects.all().order_by("-post_date")[:3]
    return render(request, "blog/index.html", {
        "posts": last_3_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-post_date")
    return render(request, "blog/all-posts.html", {
        "posts": all_posts
    })


def post_detail(request, slug):
    found_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": found_post,
        "tags": found_post.tags.all()
    })

