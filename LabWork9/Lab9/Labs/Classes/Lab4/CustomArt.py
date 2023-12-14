import logging
from colorama import Fore
from Labs.Classes.Lab3.ArtGenerator import ArtGenerator
from Data.Lab4.fonts import fonts

class CustomArt(ArtGenerator):
    #Змінні за замовчуванням для власного ASCII арту
    _font = 'standard'
    _user_height = 5
    _user_width = 5
    _direction_message = ''
    _color = Fore.WHITE

    #Словник для вибору шрифту
    _FONTS = {
        '1': 'standard',
        '2': 'banner3',
    }

    def __init__(self, message=' ', **kwargs):
        super().__init__(message)

    def _custom_justify(self):
        """Метод для вирівнювання повідомлення"""
        message = self.message
        if self.justify == 'center':
            message = message.rjust(20, ' ')
        elif self.justify == 'right':
            message = message.rjust(40)
        elif self.justify == 'left':
            message = message.ljust(0, ' ')
        return message

    def _create(self, **kwargs):
        """Метод для створення ASCII-мистецтва на основі власного шрифту"""
        try:
            font_key = kwargs.get('font', self._font)
            font = fonts.get(font_key, fonts['standard'])  #Перевірка наявності шрифта у словнику
            self._direction_message = self._custom_justify()
            art = []
            max_lines = max(len(font.get(letter, '').split('\n')) for letter in self._direction_message)
            for line_num in range(max_lines):
                line = ""
                for letter in self._direction_message:
                    letter_lines = font.get(letter, '').split('\n')
                    if line_num < len(letter_lines):
                        if self.justify == 'left':
                            line += letter_lines[line_num].ljust(len(letter_lines[0]) + 1)
                        elif self.justify == 'center':
                            line += letter_lines[line_num].center(len(letter_lines[0]) + 1)
                        elif self.justify == 'right':
                            line += letter_lines[line_num].rjust(len(letter_lines[0]) + 1)
                        else:
                            line += letter_lines[line_num].rjust(len(letter_lines[0]) + 1)
                    else:
                        line += ' ' * (len(letter_lines[0]) + 1)
                art.append(line)
            output = '\n'.join(art)
            return output
        except Exception as e:
            logging.error(f"An error occurred in CustomArt._create(): {e}")

    def save(self, filename):
        """Метод для збереження ASCII арту у файлі"""
        try:
            with open(filename, 'w') as file:
                self.create()
                file.write(self._ascii_art)
        except Exception as e:
            logging.error(f"An error occurred in CustomArt.save(): {e}")
