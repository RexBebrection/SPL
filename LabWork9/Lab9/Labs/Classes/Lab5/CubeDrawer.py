from __future__ import division
from colorama import init, Fore
import os

init(autoreset=True)

class CubeDrawer:
    def __init__(self, x_size=1, y_size=1, z_size=1, color=Fore.WHITE):
        # Ініціалізація розмірів куба та його кольору
        self.x_size = x_size
        self.y_size = y_size
        self.z_size = z_size
        self.color = color
        self.width = x_size * 2
        self.height = y_size * 2
        self.cube = [[' ']*self.width for _ in range(self.height)]

    def draw_cube(self):
        # Визначення вершин та ребер куба
        vertices = {
            'tc': (self.width//2, 0),
            'tl': (0, int(.25*self.height)),
            'tr': (self.width-1, int(.25*self.height)),
            'cc': (self.width//2, self.height//2),
            'bl': (0, int(.75*self.height)),
            'br': (self.width-1, int(.75*self.height)),
            'bc': (self.width//2, self.height-1)
        }
        edges = (
            ('tc', 'tl'),
            ('tc', 'tr'),
            ('tl', 'cc'),
            ('tl', 'bl'),
            ('tr', 'cc'),
            ('tr', 'br'),
            ('bl', 'bc'),
            ('br', 'bc'),
            ('cc', 'bc')
        )

        # Рисування кожного ребра куба
        for edge in edges:
            v1 = vertices[edge[0]]
            v2 = vertices[edge[1]]
            x1 = v1[0]
            y1 = v1[1]
            x2 = v2[0]
            y2 = v2[1]
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            try:
                m = (y2-y1)/(x2-x1)
            except ZeroDivisionError:
                c = '|'
                for yy in range(min(y1, y2), max(y1, y2)+1):
                    self.cube[yy][x1] = self.color + c
            else:
                c = '.'
                yy = y1
                for xx in range(x1, x2+1):
                    self.cube[int(yy)][xx] = c
                    yy += m

                if edge[0] in ('tc', 'tr', 'tl') and edge[1] in ('tc', 'tr', 'tl'):
                    self.cube[y1][x1] = c

        # Перетворення матриці куба у рядок
        cube_str = '\n'.join(''.join(row) for row in self.cube)
        return cube_str

    def draw_square(self, length):
        # Створення квадрата зазначеної довжини
        square_width = int(length * 2.5)
        square = [[' ']*square_width for _ in range(length)]

        # Заповнення квадрата лініями
        for i in range(length):
            for j in range(square_width):
                if i == 0 or i == length-1:
                    square[i][j] = self.color + '-'
                elif j == 0 or j == square_width-1:
                    square[i][j] = self.color + '|'

        # Перетворення матриці квадрата у рядок
        square_str = '\n'.join(''.join(row) for row in square)
        return square_str

    def remove_color_codes(self, text):
        # Видалення кодів кольору з тексту
        while '\033[' in text:
            start = text.find('\033[')
            end = text.find('m', start)
            if end != -1:
                text = text[:start] + text[end+1:]
            else:
                break
        return text

    def save_to_file(self, content):
        # Збереження тексту у файл
        filename = input("Enter the file name to save: ")
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), f"../../../Data/Lab5"))
        os.makedirs(path, exist_ok=True)

        full_path = os.path.join(path, filename)
        with open(full_path, 'w') as file:
            file.write(self.remove_color_codes(content))

        print(f"File saved successfully at: {full_path}")

    def run_cube_drawer(self):
        try:
            # Введення розмірів куба
            x_size = int(input("Enter the cube size along the x-axis: "))
            y_size = int(input("Enter the cube size along the y-axis: "))
            z_size = int(input("Enter the cube size along the z-axis: "))
        except ValueError:
            print("Invalid input format. Using default sizes (1, 1, 1).")
            x_size, y_size, z_size = 1, 1, 1

        # Вибір кольору
        selected_color = input("Enter the color code (e.g., RED, GREEN, BLUE): ")

        try:
            color_code = getattr(Fore, selected_color.upper())
        except AttributeError:
            print("Invalid color code. Using white color by default.")
            color_code = Fore.WHITE

        # Створення екземпляра класу CubeDrawer та відображення куба
        cube_drawer = CubeDrawer(x_size, y_size, z_size, color_code)
        cube_str = cube_drawer.draw_cube()
        print(cube_str)

        # Запит на збереження куба у файл
        save_cube = input("Do you want to save the cube to a file? (Yes/No): ").lower()
        if save_cube == "yes":
            cube_drawer.save_to_file(cube_str)

        # Запит на генерацію квадрата
        generate_square = input("Do you want to generate a square? (Yes/No): ").lower()

        if generate_square == "yes":
            square_str = cube_drawer.draw_square(y_size)
            print(square_str)

            # Запит на збереження квадрата у файл
            save_square = input("Do you want to save the square to a file? (Yes/No): ").lower()
            if save_square == "yes":
                cube_drawer.save_to_file(square_str)
