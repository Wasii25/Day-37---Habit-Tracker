import requests
from datetime import datetime

today = datetime(year=2024, month=10, day=12)
USER_NAME = "wasi25"
TOKEN = "cfhlsrdijghoiserhtiu"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

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

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

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

# response2 = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response2.text)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1/{today.strftime('%Y%m%d')}"


response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
