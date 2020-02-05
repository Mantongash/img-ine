from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="Home"),
  path("search/", views.search_results, name="search_results")
]