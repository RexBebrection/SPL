import math

class MathOperations:

    @staticmethod
    def sqrt(num):
        if num < 0:
            raise ValueError("Корінь з від'ємного числа неможливий.")
        return math.sqrt(num)

    @staticmethod
    def power(base, exponent):
        return base ** exponent

    @staticmethod
    def percentage(number, percent):
        return (number * percent) / 100

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Ділення на нуль неможливе.")
        return num1 / num2

    def perform_calculation(self, num1, operator, num2=None):
        if operator == '+':
            self.result = self.add(num1, num2)
        elif operator == '-':
            self.result = self.subtract(num1, num2)
        elif operator == '*':
            self.result = self.multiply(num1, num2)
        elif operator == '/':
            self.result = self.divide(num1, num2)
        elif operator == '^':
            self.result = MathOperations.power(num1, num2)
        elif operator == 'sqrt':
            self.result = MathOperations.sqrt(num1)
        elif operator == '%':
            self.result = MathOperations.percentage(num1, num2)

    def run_calculator(self, is_testing=False):
        if not is_testing:
            print("Вітаю в калькуляторі!")
            while True:
                try:
                    num1 = float(input("Введіть перше число: "))
                    operator = input("Введіть операцію (+, -, *, /, sqrt, ^, %): ")
                    if operator not in ('+', '-', '*', '/', 'sqrt', '^', '%'):
                        raise ValueError("Помилка: Введена операція недійсна. Допустимі операції: +, -, *, /, sqrt, ^, %.")
                    num2 = None
                    if operator in ('+', '-', '*', '/'):
                        num2 = float(input("Введіть друге число: "))
                    self.perform_calculation(num1, operator, num2)
                    print("Результат: {:.2f}".format(self.result))
                except ValueError as e:
                    print(f"Помилка: {e}")
                except ZeroDivisionError:
                    raise ValueError("Помилка: Ділення на нуль неможливе.")
                another_calculation = input("Виконати ще одну операцію? (Так/Ні): ")
                if another_calculation.lower() != "так":
                    print("Дякую за користування калькулятором!")
                    break
        else:
            print("Тестування калькулятора завершено.")

if __name__ == "__main__":
    calc = Calculator()
    calc.run_calculator()
