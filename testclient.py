import requests

# url = "http://127.0.0.1/upload"
# files = {"photo": open("1.PNG", "rb")}
# data = {"user_id": "6080085900", "text": "Тестовое описание"}
#
# response = requests.post(url, files=files, data=data)
# print(response.text)  # Ответ сервера
import os

# Получить абсолютный путь к текущему файлу
current_file_path = os.path.abspath(__file__)
print("Абсолютный путь к текущему файлу:", current_file_path)

# Получить только имя текущего файла
current_file_name = os.path.basename(__file__)
print("Имя текущего файла:", current_file_name)

# Получить директорию, в которой находится текущий файл
current_dir = os.path.dirname(os.path.abspath(__file__))
print("Директория текущего файла:", current_dir)