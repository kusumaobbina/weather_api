import pytest

@pytest.fixture
def sample_data():
    return {"city": "Ireland"}

@pytest.fixture
def city_data():
    return ["Ireland", "Germany", "USA"]
