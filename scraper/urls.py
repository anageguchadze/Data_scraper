from django.urls import path
from .views import scrape_planity

urlpatterns = [
    path('scrape/', scrape_planity, name="scrape"),
]