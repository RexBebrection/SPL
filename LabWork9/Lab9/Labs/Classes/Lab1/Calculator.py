# Calculator.py
from Shared.operations import Operators

class Calculate(Operators):
    def run(self):
        print("Simple Calculator")
        print("Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter the operation number: ")

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        try:
            #Виклик методу відповідно до введеної операції
            if choice == "1":
                result = self.add(num1, num2)
            elif choice == "2":
                result = self.subtract(num1, num2)
            elif choice == "3":
                result = self.multiply(num1, num2)
            elif choice == "4":
                result = self.divide(num1, num2)
            else:
                result = "Invalid operation."

            #Виведення результату
            print(f"Result: {result}")

        except ValueError as e:
            #Обробка помилок, пов'язаних із невірним введенням користувача
            print(f"Error: {e}")
        except ZeroDivisionError:
            #Обробка помилки ділення на нуль
            print("Error: Cannot divide by zero.")

if __name__ == "__main__":
    calc = Calculate()
    calc.run()
