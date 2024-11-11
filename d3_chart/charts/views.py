from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

from d3_chart.charts.mock_data import mock_data



class D3ChartView(LoginRequiredMixin, TemplateView):
    template_name = "charts/d3.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch the chart data from the database
        context["chart_data"] = mock_data
        return context


d3_chart_view = D3ChartView.as_view()


class ChartDataAPIView(LoginRequiredMixin, APIView):
    """
    API view for retrieving chart data.
    """

    def get(self, request, *args, **kwargs):
        return Response(mock_data)


chart_data_api_view = ChartDataAPIView.as_view()

