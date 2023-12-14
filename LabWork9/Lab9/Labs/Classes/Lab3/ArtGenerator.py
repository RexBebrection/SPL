import pyfiglet
from colorama import Fore
from Shared.artBase import ArtBase
import logging

class ArtGenerator(ArtBase):
    #Змінні за замовчуванням для генератора мистецтва
    _font = 'standard'
    _color = Fore.RESET
    _width = 80
    _direction = 'auto'
    _justify = 'auto'
    _user_height = None
    _user_width = None

    #Словники для вибору значень
    _FONTS = {
        '1': "standard",
        '2': "slant",
        '3': "big",
        '4': "block",
        '5': "bubble",
        '6': "digital",
        '7': "isometric1",
        '8': "isometric2",
        '9': "letters",
        '10': "script",
        '11': "shadow",
        '12': "starwars",
    }
    _COLORS = {
        'BLACK': Fore.BLACK,
        'RED': Fore.RED,
        'GREEN': Fore.GREEN,
        'YELLOW': Fore.YELLOW,
        'BLUE': Fore.BLUE,
        'MAGENTA': Fore.MAGENTA,
        'CYAN': Fore.CYAN,
        'WHITE': Fore.WHITE,
        'RESET': Fore.RESET,
    }
    _DIRECTIONS = {
        'LTR': 'left-to-right',
        'RTl': 'right-to-left',
    }
    _JUSTIFIES = {
        'CENTER': 'center',
        'RIGHT': 'right',
        'LEFT': 'left',
    }

    def create(self):
        """Метод для створення ASCII арту"""
        try:
            art = pyfiglet.Figlet(font=self._font, direction=self._direction, justify=self._justify, width=self._width)
            self._ascii_art = self._color + art.renderText(self._message)
        except Exception as e:
            logging.error(f"An error occurred in ArtGenerator.create(): {e}")

    def prev_view(self):
        """Метод для перегляду попереднього створеного ASCII арту"""
        return self._ascii_art

    def _art_zoom(self):
        """Метод для збільшення ASCII арту"""
        return self.create(font='banner3')

    def zoom(self):
        """Метод для зміни розміру ASCII арту"""
        try:
            line = ''
            lines = []
            len_line = 0
            mx = 0
            art = self._art_zoom()
            for i in art:
                if i != '\n':
                    line += i
                    mx += 1
                else:
                    if len_line < mx:
                        len_line = mx
                    mx = 0
                    lines += [line]
                    line = ''
            len_lines = len(lines)
            square_base = len_lines * len_line
            square_update = self._user_height * self._user_width
            if square_update >= square_base:
                pw = round(square_update / square_base)
            else:
                pw = round(square_base / square_update)
            new_lines = []
            for line in lines:
                new_line = ''
                for ln in line:
                    new_line += ln
                    new_line += ln
                new_lines += [new_line] * pw
            laq = ''
            for line in new_lines:
                laq += line + '\n'
            self._ascii_art = laq
        except Exception as e:
            logging.error(f"An error occurred in ArtGenerator.zoom(): {e}")

    def __str__(self):
        """Метод для отримання рядкового представлення ASCII арту"""
        return self._ascii_art

    #GET/SET MESSAGE
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    #GET/SET FONT
    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font = value

    #GET/SET COLOR
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    #GET/SET WIDTH
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    #GET/SET DIRECTION
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    #GET/SET JUSTIFY
    @property
    def justify(self):
        return self._justify

    @justify.setter
    def justify(self, value):
        self._justify = value

    #GET/SET User height
    @property
    def user_height(self):
        return self._user_height

    @user_height.setter
    def user_Aheight(self, value):
        self._user_height = value

    #GET/SET User height
    @property
    def user_width(self):
        return self._user_width

    @user_width.setter
    def user_width(self, value):
        self._user_width = value
