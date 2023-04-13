import requests

with open('imgs/dog.jpg', 'rb') as f:
    dog_bytes = f.read()

resp = requests.post("http://localhost:8000/", data=dog_bytes)
print(resp.json())
# {'class_index': 258}
