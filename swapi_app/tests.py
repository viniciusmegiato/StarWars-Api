from unittest.mock import patch
from django.http import Http404
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from .views import get_character


class CharacterTestCase(TestCase):
    def test_get_character_by_id(self):
        factory = APIRequestFactory() # Create a factory to generate requests
        request = factory.get('/characters/1') # Create a GET request to /characters/1
        response = get_character(request, 1) # Call the view function with the request
        
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Check if the response status code is 200
        self.assertEqual(len(response.data['related']), 3) # Check if the response contains 3 related entities
        self.assertTrue(all('id' in entity and 'name' in entity and 'relation' in entity for entity in response.data['related'])) # Check if each related entity has the required fields

    @patch('swapi_app.views.SWAPIService.fetch_data_by_id')
    def test_get_character_not_found(self, mock_fetch_data_by_id):
        # Mock the fetch_data_by_id function to raise an Http404 exception
        mock_fetch_data_by_id.side_effect = Http404

        factory = APIRequestFactory() # Create a factory to generate requests
        request = factory.get('/characters/999') # Create a GET request to /characters/999
        response = get_character(request, 999) # Call the view function with the request

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND) # Check if the response status code is 404
        self.assertEqual(response.data, {'error': 'Character not found'}) # Check if the response contains the correct error message
