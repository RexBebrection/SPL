import requests
from PIL import Image
from io import BytesIO
from tabulate import tabulate
from prettytable import PrettyTable
import signal
import sys
from colorama import Fore, init
import json
import csv

init(autoreset=True)

class DogAPI:
    base_url = "https://api.thedogapi.com/v1"

    def __init__(self, api_key):
        self.headers = {"x-api-key": api_key}

class DisplayDogApi:
    BASE_URL = "https://dog.ceo/api"

    @classmethod
    def get_all_breeds(cls):
        response = requests.get(f"{cls.BASE_URL}/breeds/list/all")
        data = response.json()
        breeds = data.get("message", {})
        return breeds.keys()

    @classmethod
    def get_random_image(cls, breed):
        response = requests.get(f"{cls.BASE_URL}/breed/{breed}/images/random")
        data = response.json()
        image_url = data.get("message", "")
        return image_url

class ConsoleInterface:
    def display_table(self, data, color):
        headers = [Fore.RESET + color + "DogBreed", Fore.RESET + color + "PictureUrl"]
        rows = [(color + breed, DisplayDogApi.get_random_image(breed)) for breed in data]
        table = tabulate(rows, headers, tablefmt="grid")
        print(table)

    def display_list(self, data, color):
        for breed in data:
            print(color + f"{breed}: {DisplayDogApi.get_random_image(breed)}")

    def display_image(self, image_url):
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.show()

    def remove_color_codes(self, text):
        while '\033[' in text:
            start = text.find('\033[')
            end = text.find('m', start)
            if end != -1:
                text = text[:start] + text[end+1:]
            else:
                break
        return text

    def save_to_json(self, data, filename):
        data_to_save = [{"DogBreed": breed, "PictureUrl": DisplayDogApi.get_random_image(breed)} for breed in data]
        with open(filename, 'w') as file:
            json.dump(data_to_save, file, indent=2)
        print(f"Data saved to {filename} in JSON format.")


    def save_to_csv(self, data, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([Fore.RESET + "DogBreed", Fore.RESET + "PictureUrl"])
            for breed in data:
                writer.writerow([self.remove_color_codes(breed), self.remove_color_codes(DisplayDogApi.get_random_image(breed))])
        print(f"Data saved to {filename} in CSV format.")


    def save_to_txt(self, data, filename):
        with open(filename, 'w') as file:
            for breed in data:
                file.write(f"{self.remove_color_codes(breed)}: {self.remove_color_codes(DisplayDogApi.get_random_image(breed))}\n")
        print(f"Data saved to {filename} in TXT format.")

def signal_handler(sig, frame):
    print("You pressed Ctrl+C!")
    sys.exit(0)

def choose_display_format():
    while True:
        print("Choose a display format:")
        print("1. Table")
        print("2. List")
        format_choice = input("Enter the number of the display format: ")

        if format_choice in ("1", "2"):
            return format_choice
        else:
            print("Invalid display format. Please enter 1 or 2.")

def choose_color():
    while True:
        print("Choose a color:")
        print("1. Red")
        print("2. Green")
        print("3. Yellow")
        color_choice = input("Enter the number of the color: ")

        if color_choice == "1":
            return Fore.RED
        elif color_choice == "2":
            return Fore.GREEN
        elif color_choice == "3":
            return Fore.YELLOW
        else:
            print("Invalid color choice. Please enter 1, 2, or 3.")

def start_menu():
    print("Hello! Choose the option:")
    print("1. Continue")
    print("2. Exit")
    option = input("Enter the number of the option: ")
    return option

def main():
    api_key = "live_erHxdDaDlKKkhVAn0IpEIPT9trh9HzJx"
    dog_api = DogAPI(api_key)
    interface = ConsoleInterface()

    while True:
        user_option = start_menu()

        if user_option == "1":
            breeds = DisplayDogApi.get_all_breeds()

            color = choose_color()
            format_choice = choose_display_format()

            if format_choice == "1":
                interface.display_table(breeds, color)
            elif format_choice == "2":
                interface.display_list(breeds, color)

            save_choice = input("Do you want to save the data? (y/n): ")
            if save_choice.lower() == 'y':
                save_format = input("Choose a save format:\n1. JSON\n2. CSV\n3. TXT\nEnter the number of the save format: ")
                save_filename = input("Enter the filename: ")
                if save_format == "1":
                    interface.save_to_json(breeds, save_filename)
                elif save_format == "2":
                    interface.save_to_csv(breeds, save_filename)
                elif save_format == "3":
                    interface.save_to_txt(breeds, save_filename)
                else:
                    print("Invalid save format. Please enter 1, 2, or 3.")

            repeat_choice = input("Do you want to perform another operation? (y/n): ")
            if repeat_choice.lower() != 'y':
                break
        elif user_option == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1 or 2.")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
