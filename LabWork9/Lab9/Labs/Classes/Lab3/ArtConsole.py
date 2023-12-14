from Labs.Classes.Lab3.ArtGenerator import ArtGenerator

class ArtConsole(ArtGenerator):

    @classmethod
    def set_parameters(cls, dct, input_message):
        """Метод для вибору параметрів з переданого словника"""
        for key, value in dct.items():
            print(f"{key}: {value}")
        value = input(f"Select {input_message}: ")
        current_value = dct.get(value, None)
        if current_value:
            return current_value
        else:
            return None

    def input_function(self, dct, input_message, default):
        """Метод для введення значення параметра користувачем"""
        check = input(f"Do you want to set {input_message}? (1/0): ")
        font = None
        if check == '1':
            font = self.set_parameters(dct, input_message)
        if font:
            return font
        else:
            return default

    def configuration(self):
        """Метод для конфігурації параметрів генератора"""
        try:
            message = input("Input message: ")
            self.message = message
            self.font = self.input_function(self._FONTS, 'font', self.font)
            self.color = self.input_function(self._COLORS, 'color', self.color)
            self.justify = self.input_function(self._JUSTIFIES, 'justify', self.justify)
            self.direction = self.input_function(self._DIRECTIONS, 'direction', self.direction)

            #Зміна власного шрифту
            change_font = input('Do you want to create your own font? (1/0): ')
            if change_font == '1':
                custom_symbol = input("Input custom symbol: ")
                self.set_custom_font(custom_symbol)

            #Зміна параметрів масштабування (zoom)
            change_zoom = input('Do you want to create zoom? (1/0): ')
            if change_zoom == '1':
                height = int(input("Input custom height: "))
                width = int(input("Input custom width: "))
                self.user_height = height
                self.user_width = width
                self.zoom()

            #Перегляд та збереження зображення
            watch = input("Do you want to watch art before saving? (1/0): ")
            if watch == '1':
                if self._ascii_art:
                    print(self._ascii_art)
                else:
                    print(self.prev_view())
                check = input("Do you want to save? (1/0): ")
                if check == '1':
                    save = input("Input filename: ")
                    self.save(f"Lab9/Data/Lab3/{save}")

        except Exception as e:
            print(e)

    def run(self):
        """Метод для виконання основної логіки програми"""
        stop = ''
        while stop != 'f':
            try:
                self.configuration()
                self.create()
                print(self)
            except Exception as e:
                print(e)
            finally:
                stop = input("Press 'f' if you want to exit: ")

if __name__ == "__main__":
    art = ArtConsole()
    art.run()
