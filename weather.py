import requests

def get_data(city):
    url = f"https://wttr.in/{city}"
    response = requests.get(url)
    return response.status_code

data = get_data("Ireland")
print("Status Code:", data)
