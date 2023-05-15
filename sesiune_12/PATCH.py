import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {
    "title": "foo",
}

'''
                                !!!!!!!!!!!!!!!!!
Spre deosebire de PUT, PATCH atualizeaza doar campurile care apar in payload.
                                !!!!!!!!!!!!!!!!!
'''

response = requests.patch(url, payload)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}.")