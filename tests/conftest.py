# tests/conftest.py
import pytest
from unittest.mock import Mock

# tests/conftest.py
import pytest

# Fixture for a single city
@pytest.fixture
def sample_data():
    return { "city": "Ireland" }

# Fixture for multiple cities (parameterized)
@pytest.fixture
def city_data():
    return [
        { "city": "Ireland" },
        { "city": "London" },
        { "city": "New York" },
        { "city": "Tokyo" }
    ]

# Mock for a successful response
@pytest.fixture
def mock_success_response():
    mock_response = Mock()
    mock_response.status_code = 200
    return mock_response

# Mock for a 404 error response
@pytest.fixture
def mock_404_response():
    mock_response = Mock()
    mock_response.status_code = 404
    return mock_response

# Mock for a timeout error response
@pytest.fixture
def mock_timeout_response():
    mock_response = Mock()
    mock_response.side_effect = requests.exceptions.Timeout("Request timed out")
    return mock_response
