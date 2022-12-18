from django.test import TestCase
from django.urls import reverse
from .models import Snack

class SnackViewTests(TestCase):
    def test_snack_list_view(self):
        # Send a GET request to the snack list view
        response = self.client.get(reverse('snack_list'))

        # Check that the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is being used
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_snack_detail_view(self):
        
        url = reverse('snacks')
        response = self.client.get(url)
        print(response)

        # Check that the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is being used
        self.assertTemplateUsed(response, 'snack_detail.html')
