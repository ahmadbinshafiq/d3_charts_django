from django.urls import path

from .views import chart_data_api_view
from .views import d3_chart_view

app_name = "users"
urlpatterns = [
    path("chart/", d3_chart_view, name="chart"),
    path("api/chart-data/", chart_data_api_view, name="chart-data-api"),
]
