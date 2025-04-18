# tests/test_weather.py
import unittest
import requests
from unittest.mock import patch, Mock
from weather import get_data

class TestWeatherAPI(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.sample_data = { "city": "Ireland" }
        self.city_data = [
            { "city": "Ireland" },
            { "city": "London" },
            { "city": "New York" },
            { "city": "Tokyo" }
        ]

    @patch('requests.get')
    def test_get_data(self, mock_get):
        # Simulate a successful 200 response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        city = self.sample_data["city"]
        result = get_data(city)
        self.assertEqual(result, 200)

    @patch('requests.get')
    def test_get_data_with_multiple_cities(self, mock_get):
        # Simulate a successful response for all cities
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Testing multiple cities
        for city_info in self.city_data:
            city = city_info["city"]
            result = get_data(city)
            self.assertEqual(result, 200)

    @patch('requests.get')
    def test_get_data_http_error(self, mock_get):
        # Simulate a 404 error response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        city = self.sample_data["city"]
        result = get_data(city)
        self.assertEqual(result, 404)

    @patch('requests.get')
    def test_get_data_timeout_error(self, mock_get):
        # Simulate a timeout error
        mock_get.side_effect = requests.exceptions.Timeout("Request timed out")
        
        city = self.sample_data["city"]
        result = get_data(city)
        self.assertTrue("timed out" in result)

    @patch('requests.get')
    def test_get_data_network_error(self, mock_get):
        # Simulate a network error
        mock_get.side_effect = requests.exceptions.ConnectionError("No internet")
        
        city = self.sample_data["city"]
        result = get_data(city)
        self.assertTrue("No internet" in result)

if __name__ == '__main__':
    unittest.main()
