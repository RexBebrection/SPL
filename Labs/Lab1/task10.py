import math

class Calculator:
    def __init__(self):
        self.memory = None  # Зберігання в пам'яті
        self.history = []  # Список для зберігання історії
        self.decimal = 2

    def perform_calculation(self, num1, operator, num2=None):
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Помилка: ділення на нуль"
        elif operator == "^":
            result = num1 ** num2
        elif operator == "sqrt":
            if num1 >= 0:
                result = math.sqrt(num1)
            else:
                result = "Помилка: корінь з від'ємного числа"
        elif operator == "%":
            if num2 != 0:
                result = num1 % num2
            else:
                result = "Помилка: ділення на нуль"
        else:
            result = "Помилка"

        if isinstance(result, float):
            result = round(result, self.decimal)

        return result

    def run_calculator(self):
        while True:
            num1 = float(input("Введіть перше число: "))
            operator = input("Введіть оператор (+, -, *, /, ^, sqrt, %): ")

            while True:
                if operator in ('+', '-', '*', '/', 'sqrt', '^', '%'):
                    break
                else:
                    print("Помилка: невірний оператор")
                    operator = input("Введіть оператор (+, -, *, /, ^, sqrt, %): ")

            if operator in ('+', '-', '*', '/', '^', '%'):
                num2 = float(input("Введіть друге число: "))
            else:
                num2 = None

            if operator == "settings":
                self.handle_settings()
                continue

            result = self.perform_calculation(num1, operator, num2)

            # Додавання до історії
            if num2 is not None:
                self.history.append(f"{num1} {operator} {num2} = {result}")
            else:
                self.history.append(f"{num1} {operator} = {result}")

            print(f"Результат: {result}")

            newcalc = input("Продовжити: '+' (settings/history/exit) Введіть операцію:")
            if newcalc.lower() != '+':
                if newcalc.lower() == 'settings':
                    self.handle_settings()
                elif newcalc.lower() == 'history':
                    self.show_history()
                elif newcalc.lower() == 'exit':
                    break

    def handle_settings(self):
        print("Налаштування:")
        print(f"1. Кількість десяткових розрядів (зараз {self.decimal}):")
        print(f"2. Зберігання результату в пам'яті (зараз {'Включено' if self.memory is not None else 'Виключено'}):")
        setting_choice = input("Виберіть опцію (1/2): ")
        if setting_choice == "1":
            self.decimal = int(input("Введіть нову кількість десяткових розрядів: "))
        elif setting_choice == "2":
            if self.memory is not None:
                self.memory = None
                print("Зберігання результату в пам'яті вимкнено.")
            else:
                self.memory = result
                print(f"Збережено результат в пам'яті: {self.memory}")
        else:
            print("Невірний вибір налаштувань.")

    def show_history(self):
        print("Історія обчислень:")
        for entry in self.history:
            print(entry)

def main():
    calc = Calculator()
    calc.run_calculator()

if __name__ == "__main__":
    main()
