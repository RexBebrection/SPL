import requests
from colorama import Fore
from tabulate import tabulate
from PIL import Image
from io import BytesIO
import json
import csv
import os

class DogAPI:
    base_url = "https://api.thedogapi.com/v1"

    def __init__(self, api_key):
        # Ініціалізація об'єкта DogAPI з використанням ключа API
        self.headers = {"x-api-key": api_key}

class DisplayDogApi:
    BASE_URL = "https://dog.ceo/api"

    @classmethod
    def get_all_breeds(cls):
        # Отримати список всіх порід собак
        response = requests.get(f"{cls.BASE_URL}/breeds/list/all")
        data = response.json()
        breeds = data.get("message", {})
        return breeds.keys()

    @classmethod
    def get_random_image(cls, breed):
        # Отримати випадкове зображення для певної породи собаки
        response = requests.get(f"{cls.BASE_URL}/breed/{breed}/images/random")
        data = response.json()
        image_url = data.get("message", "")
        return image_url

class ConsoleInterface:
    def display_table(self, data, color):
        # Відображення даних у вигляді таблиці
        headers = [Fore.RESET + color + "DogBreed", Fore.RESET + color + "PictureUrl"]
        rows = [(color + breed, DisplayDogApi.get_random_image(breed)) for breed in data]
        table = tabulate(rows, headers, tablefmt="grid")
        print(table)

    def display_list(self, data, color):
        # Відображення даних у вигляді списку
        for breed in data:
            print(color + f"{breed}: {DisplayDogApi.get_random_image(breed)}")

    def display_image(self, image_url):
        # Відображення зображення за URL
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.show()

    def remove_color_codes(self, text):
        # Видалення кодів кольорів з тексту
        while '\033[' in text:
            start = text.find('\033[')
            end = text.find('m', start)
            if end != -1:
                text = text[:start] + text[end+1:]
            else:
                break
        return text

    def save_to_json(self, data, filename):
        # Збереження даних у форматі JSON
        save_directory = os.path.abspath(os.path.join("Lab9", "Data", "Lab7"))
        os.makedirs(save_directory, exist_ok=True)
        save_path = os.path.join(save_directory, filename)
        data_to_save = [{"DogBreed": breed, "PictureUrl": DisplayDogApi.get_random_image(breed)} for breed in data]
        with open(save_path, 'w') as file:
            json.dump(data_to_save, file, indent=2)
        print(f"Дані збережено у файл {save_path} у форматі JSON.")

    def save_to_csv(self, data, filename):
        # Збереження даних у форматі CSV
        save_directory = os.path.abspath(os.path.join("Lab9", "Data", "Lab7"))
        os.makedirs(save_directory, exist_ok=True)
        save_path = os.path.join(save_directory, filename)
        with open(save_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([Fore.RESET + "DogBreed", Fore.RESET + "PictureUrl"])
            for breed in data:
                writer.writerow([self.remove_color_codes(breed), self.remove_color_codes(DisplayDogApi.get_random_image(breed))])
        print(f"Дані збережено у файл {save_path} у форматі CSV.")

    def save_to_txt(self, data, filename):
        # Збереження даних у форматі TXT
        save_directory = os.path.abspath(os.path.join("Lab9", "Data", "Lab7"))
        os.makedirs(save_directory, exist_ok=True)
        save_path = os.path.join(save_directory, filename)
        with open(save_path, 'w') as file:
            for breed in data:
                file.write(f"{self.remove_color_codes(breed)}: {self.remove_color_codes(DisplayDogApi.get_random_image(breed))}\n")
        print(f"Дані збережено у файл {save_path} у форматі TXT.")
