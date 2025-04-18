import unittest
from unittest.mock import patch, Mock
from weather import get_data

class TestGetData(unittest.TestCase):
    @patch('requests.get') 
    def test_get_data(self, mock_get):

        mock_response = Mock()
        mock_response.status_code = 200 
        mock_get.return_value = mock_response
        result = get_data("Ireland")
        self.assertEqual(result, 200)
  
if __name__ == '__main__': 
    unittest.weather(argv=['first-arg-is-ignored'], exit=False) 