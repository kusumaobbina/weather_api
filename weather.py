import requests

def get_data(city):
    url = "https://wttr.in/"+city
    response = requests.get(url)
    print("Status Code:", response.status_code)
    return response.status_code

get_data("Ireland")
