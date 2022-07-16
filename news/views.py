from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View
from django.shortcuts import render

from .forms import CommentForm
from .models import New

# Create your views here.

class StartingPageView(ListView):
    template_name = "news/index.html"
    model = New
    

    def get_context_data(self, **kwargs):
        all_news = New.objects.all()
        context = super().get_context_data(**kwargs)
        context["news"] = all_news.order_by("-id")
        return context


# def first_news(request):
#     news = New.objects.all()
#     return render(request, "news/index.html", {
#         "news": news
#     })


class NewsDetailsView(View):
    template_name = "news/news-details.html"
    model = New
    context_object_name = "news"

    def get(self, request, slug):
        single_news = New.objects.get(slug=slug)
        context = {
            "news": single_news,
            "comment_form": CommentForm(),
            "comments": single_news.comments.all().order_by("-id")
        }
        return render(request, "news/news-details.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        single_news = New.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.new = single_news
            comment.save()

            return HttpResponseRedirect(reverse("news-details", args=[slug]))
        context = {
            "news": single_news,
            "comment_form": comment_form,
            "comments": single_news.comments.all().order_by("-id")
        }
        return render(request, "news/news-details.html", context)

# def news_details(request, slug):
#     news = New.objects.get(slug=slug)
#     return render(request, "news/news-details.html", {
#         "news": news
#     })

class WarInUkraineView(ListView):
    template_name = "news/war-in-ukraine.html"
    model = New
    context_object_name = "news"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset.filter(category=2)
        return data

# def war_in_ukraine_category(request):
#     news = New.objects.filter(category=2)
#     return render(request, "news/war-in-ukraine.html", {
#         "news": news
#     })

class SportView(ListView):
    template_name = "news/sport.html"
    model = New
    context_object_name = "news"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset.filter(category=3)
        return data

# def sport(request):
#     news = New.objects.filter(category=3)
#     return render(request, "news/sport.html", {
#         "news": news
#     })

class CultureView(ListView):
    template_name = "news/culture.html"
    model = New
    context_object_name = "news"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset.filter(category=4)
        return data

# def culture(request):
#     news = New.objects.filter(category=4)
#     return render(request, "news/culture.html", {
#         "news": news
#     })