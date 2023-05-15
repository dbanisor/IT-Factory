import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post(url, payload)
if response.status_code == 201:  # 201: created
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}.")