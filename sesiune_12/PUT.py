import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

'''
                                        !!!!!!!!!!!!!!!!!
PUT trebuie sa contina toate campurile cand se vrea o modificare altfel inlocuieste intreaga resursa: 
ex daca trecem doar title in payload, va sterge celelalte campuri.
                                        !!!!!!!!!!!!!!!!!
'''

response = requests.put(url, payload)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}.")
