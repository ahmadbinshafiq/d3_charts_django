from rest_framework.test import APITestCase
from rest_framework import status

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from d3_chart.charts.views import D3ChartView

User = get_user_model()


class ChartDataAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.url = reverse('d3_chart:chart-data-api')

    def test_chart_data_api_unauthentication(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_chart_data_api_authentication(self):
        self.client.login(username='testuser', password='password')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_chart_data_api_response(self):
        self.client.login(username='testuser', password='password')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = [
            {"label": "Category A", "value": 30},
            {"label": "Category B", "value": 80},
            {"label": "Category C", "value": 45},
            {"label": "Category D", "value": 60},
            {"label": "Category E", "value": 20},
            {"label": "Category F", "value": 90},
            {"label": "Category G", "value": 55},
        ]
        self.assertEqual(response.json(), expected_data)


class D3ChartViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_chart_view_renders_correct_template(self):
        response = self.client.get(reverse('d3_chart:chart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'charts/d3.html')

    def test_chart_view_context_data(self):
        response = self.client.get(reverse('d3_chart:chart'))
        self.assertEqual(response.status_code, 200)

        chart_data = response.context['chart_data']
        expected_data = [
            {"label": "Category A", "value": 30},
            {"label": "Category B", "value": 80},
            {"label": "Category C", "value": 45},
            {"label": "Category D", "value": 60},
            {"label": "Category E", "value": 20},
            {"label": "Category F", "value": 90},
            {"label": "Category G", "value": 55},
        ]
        self.assertEqual(chart_data, expected_data)
