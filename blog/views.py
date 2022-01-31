from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def starting_page(request):
    return HttpResponse("List of latest 3 blogs")


def posts(request):
    return HttpResponse("List of latest all blogs")


def post_detail(request):
    return HttpResponse("Post detail")

