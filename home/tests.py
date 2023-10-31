"""
Home App - Tests
----------------
Tests for Home App.
"""


from django.test import TestCase


class TestViews(TestCase):
    """
    Unit Tests for Home App Views
    """

    def test_home_page(self):
        """Test if home page renders correct page when user is
        authenticated as client user"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    def test_home_page_neauthenticated(self):
        """Test if home page renders correct page
        without user authentication"""
        self.client.logout()
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
