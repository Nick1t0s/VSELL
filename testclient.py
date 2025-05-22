import requests

url = "http://127.0.0.1/upload"
files = {"photo": open("1.PNG", "rb")}
data = {"user_id": "6080085900", "text": "Тестовое описание"}

response = requests.post(url, files=files, data=data)
print(response.text)  # Ответ сервера