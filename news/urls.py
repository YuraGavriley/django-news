from . import views
from django.urls import path

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("war-in-urkaine", views.WarInUkraineView.as_view(), name="war-in-ukraine"),
    path("sport", views.SportView.as_view(), name="sport"),
    path("culture", views.CultureView.as_view(), name="culture"),
    path("<slug:slug>", views.NewsDetailsView.as_view(), name="news-details")
]
