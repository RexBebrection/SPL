import math

class MathOperations():
    def sqrt(num):
        #Завдання 6.1 Обробка помилок
        if num < 0:
            raise ValueError("Корінь з від'ємного числа неможливий.")
        return math.sqrt(num)

    def power(base, exponent):
        return base ** exponent

    def percentage(number, percent):
        return (number * percent) / 100

#Завдання 1. Створення класу.
class Calculator:
    #Завдання 2. Ініціалізація калькулятора.
    def __init__(self):
        self.result = None

    #Завдання 3: Введення користувача
    def get_user_input(self):
        try:
            #Завдання 8. Десяткові числа (float)
            self.num1 = float(input("Введіть перше число: "))
            #Завдання 9. Додаткові операції
            self.operator = input("Введіть операцію (+, -, *, /, sqrt, ^, %): ")
        except ValueError:
            print("Помилка: Введене значення має бути числом.")
            return False
        return True

    #Завдання 4. Валідність оператора
    def is_valid_operator(self):
        valid_operators = ('+', '-', '*', '/', 'sqrt', '^', '%')
        if self.operator in valid_operators:
            return True
        else:
            print("Помилка: Введена операція недійсна. Допустимі операції: +, -, *, /, sqrt, ^, %.")
            return False

    #Завдання 5. Обчислення
    def calculate(self):
        if self.is_valid_operator():
            if self.operator == '+':
                self.num2 = float(input("Введіть друге число: "))
                self.result = self.num1 + self.num2
            elif self.operator == '-':
                self.num2 = float(input("Введіть друге число: "))
                self.result = self.num1 - self.num2
            elif self.operator == '*':
                self.num2 = float(input("Введіть друге число: "))
                self.result = self.num1 * self.num2
            elif self.operator == '/':
                self.num2 = float(input("Введіть друге число: "))
                #Завдання 6.2 Обробка помилок
                if self.num2 == 0:
                    print("Помилка: Ділення на нуль неможливе.")
                else:
                    self.result = self.num1 / self.num2
            elif self.operator == '^':
                self.num2 = float(input("Введіть ступінь: "))
                self.result = MathOperations.power(self.num1, self.num2)
            elif self.operator == 'sqrt':
                self.result = MathOperations.sqrt(self.num1)
            elif self.operator == '%':
                self.num2 = float(input("Введіть число для відсотків: "))
                self.result = MathOperations.percentage(self.num1, self.num2)
            return True
        return False

    #Завдання 7. Повторення обчислень
    #Завдання 10. зрозумілий інтерфейс
    def run_calculator(self):
        print("Вітаю в калькуляторі!")
        while True:
            if self.get_user_input():
                if self.calculate():
                    print("Результат: {:.2f}".format(self.result))
            another_calculation = input("Виконати ще одну операцію? (Так/Ні): ")
            if another_calculation.lower() != "так":
                print("Дякую за користуванням калькулятором!")
                break
