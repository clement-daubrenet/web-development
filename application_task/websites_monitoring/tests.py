from django.urls import reverse
from django.test import Client, TestCase


class TestViews(TestCase):
    """
    Testing http code (200) and template chosen for each view.
    """
    def setUp(self):
        self.client = Client()

    def test_general_sites_view(self):
        """
        Testing the general view of websites
        """
        url = reverse("general-sites")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                "websites_monitoring/sites.html")

    def test_summary_average(self):
        """
        Testing the average summary view
        """
        url = reverse("summary-average")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                "websites_monitoring/summary-average.html")

    def test_summary_sum(self):
        """
        Testing the sum summary view
        """
        url = reverse("summary-sum")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                "websites_monitoring/summary.html")
