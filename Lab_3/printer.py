import pyfiglet
from colorama import init, Fore

class ASCIIArtGenerator:
    def __init__(self):
        self.text = ""
        self.font = "standard"
        self.color = Fore.WHITE
        self.width = 80
        self.height = 20
        self.character = "@"

    def get_user_input(self):
        self.text = input("Enter a word or phrase: ")

    def choose_font(self):
        fonts = ["standard", "banner", "big", "block", "doom", "slant"]
        print("Available fonts:")
        for font in fonts:
            print(font)
        self.font = input("Choose a font: ").lower()
        if self.font not in fonts:
            print("Invalid font choice. Using default (standard).")

    def choose_color(self):
        print("Available colors: RED, BLUE, GREEN, YELLOW, WHITE, etc.")
        color_choice = input("Choose a color: ").upper()
        if hasattr(Fore, color_choice):
            self.color = getattr(Fore, color_choice)
        else:
            print("Invalid color choice. Using default (WHITE).")

    def choose_art_size(self):
        self.width = int(input("Enter the width of the ASCII art: "))
        self.height = int(input("Enter the height of the ASCII art: "))

    def generate_ascii_art(self):
        ascii_art = pyfiglet.Figlet(font=self.font).renderText(self.text)
        formatted_ascii_art = self.format_ascii_art(ascii_art)
        return formatted_ascii_art

    def format_ascii_art(self, ascii_art):
        lines = ascii_art.split('\n')
        formatted_art = ""
        for line in lines:
            formatted_art += line.center(self.width) + "\n"
        return formatted_art

    def preview_ascii_art(self, ascii_art):
        print("Preview of the ASCII art:")
        print(self.color + ascii_art)

    def save_to_file(self, ascii_art):
        filename = input("Enter the file name for saving (with .txt extension): ")
        with open(filename, "w") as file:
            file.write(ascii_art)
        print(f"ASCII art saved to the file {filename}")

if __name__ == "__main__":
    init(autoreset=True)  # Initialize colorama for automatic color reset
    generator = ASCIIArtGenerator()

    generator.get_user_input()
    generator.choose_font()
    generator.choose_color()
    generator.choose_art_size()

    ascii_art = generator.generate_ascii_art()
    generator.preview_ascii_art(ascii_art)
    generator.save_to_file(ascii_art)
