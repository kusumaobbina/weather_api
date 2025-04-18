import unittest
from unittest.mock import patch, Mock
from weather import get_data
from conftest import sample_data


@patch('requests.get') 
def test_get_data(mock_get, sample_data):

    mock_response = Mock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response 

    city = sample_data["city"]
    result = get_data(city)
    assert result == 200