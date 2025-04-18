import pytest
from unittest.mock import patch, Mock
from weather import get_data

# Test for single city data
@patch('requests.get')
def test_get_data(mock_get, sample_data):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    city = sample_data["city"]
    result = get_data(city)
    assert result == 200

# Test for HTTP error
@patch('requests.get')
def test_get_data_http_error(mock_get, sample_data):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    city = sample_data["city"]
    result = get_data(city)
    assert result == 404

# Test for timeout error
@patch('requests.get')
def test_get_data_timeout_error(mock_get, sample_data):
    mock_get.side_effect = TimeoutError("Request timed out")

    city = sample_data["city"]
    with pytest.raises(TimeoutError):
        get_data(city)

# Test for multiple cities data
@patch('requests.get')
def test_get_data_with_multiple_cities(mock_get, city_data):
    for city in city_data:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        result = get_data(city)
        assert result == 200
