import unittest
from unittest.mock import patch, Mock
from weather import get_data

class TestWeatherAPI(unittest.TestCase):

    @patch('requests.get')
    def test_get_data(self, mock_get, sample_data):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        city = sample_data["city"]
        result = get_data(city)
        self.assertEqual(result, 200)

    @patch('requests.get')
    def test_get_data_http_error(self, mock_get, sample_data):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        city = sample_data["city"]
        result = get_data(city)
        self.assertEqual(result, 404)

    @patch('requests.get')
    def test_get_data_timeout_error(self, mock_get, sample_data):
        mock_get.side_effect = TimeoutError("Request timed out")

        city = sample_data["city"]
        with self.assertRaises(TimeoutError):
            get_data(city)

    @patch('requests.get')
    def test_get_data_with_multiple_cities(self, mock_get, city_data):
        for city in city_data:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_get.return_value = mock_response

            result = get_data(city)
            self.assertEqual(result, 200)
