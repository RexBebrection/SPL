from colorama import Fore
from Labs.Classes.Lab3.ArtConsole import ArtConsole
from Labs.Classes.Lab4.CustomArt import CustomArt

class CustomArtConsole(CustomArt, ArtConsole):
    def __init__(self, message=' ', **kwargs):
        super().__init__(message)

    def configuration(self):
        try:
            # Запит на введення повідомлення
            message = input("Input message: ")
            self.message = message

            #Запит на вибір шрифту, кольору та вирівнювання
            self.font = self.input_function(self._FONTS, 'font', self.font)
            self.color = self.input_function(self._COLORS, 'color', self.color)
            self.justify = self.input_function(self._JUSTIFIES, 'justify', self.justify)

            #Запит на створення власного шрифту
            change_font = input('do you want to create own font? (1/0): ')
            if change_font == '1':
                custom_symbol = input("Input custom symbol: ")
                self.set_custom_font(custom_symbol)

            #Запит на створення ефекту збільшення (zoom)
            change_zoom = input('do you want to create zoom? (1/0): ')
            if change_zoom == '1':
                height = int(input("Input custom height: "))
                width = int(input("Input custom width: "))
                self.user_height = height
                self.user_width = width
                self.zoom()

            # Перевірка бажання переглянути арт перед збереженням
            watch = input("do you want to watch art before to save? (1/0):")
            if watch == '1':
                if self._ascii_art:
                    print(self._ascii_art)
                else:
                    print(self.prev_view())

                # Перевірка бажання зберегти арт
                check = input("do you want to save? (1/0): ")
                if check == '1':
                    save = input("Input filename: ")
                    self.save(f"Data/Lab4/{save}")
        except Exception as e:
            print(e)
