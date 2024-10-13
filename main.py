import requests
from datetime import datetime

today = datetime(year=2024, month=10, day=12)
USER_NAME = "<YOUR PIXELA USERNAME>"
TOKEN = "<YOUR PIXELA TOKEN>"
pixela_endpoint = "<PIXELA ENDPOINT>"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1"

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20"
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)


update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "30"
}


delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1/{today.strftime('%Y%m%d')}"


response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
