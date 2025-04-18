# weather.py
import requests

def get_data(city):
    url = f"https://wttr.in/{city}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

data = get_data("London")
print(data)