
import math
from Labs.Classes.Lab1.Calculator import Calculate as Lab1Calculator

class ClassBasedCalculator(Lab1Calculator):
    def power(self, base, exponent):
        return base ** exponent

    def sqrt(self, num):
        if num < 0:
            raise ValueError("Корінь з від'ємного числа неможливий.")
        return math.sqrt(num)

    def run_class_based_calculator(self):
        print("Class-Based Calculator")
        print("Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")

        choice = input("Enter the operation number: ")

        num1 = float(input("Enter the first number: "))

        if choice in ('1', '2', '3', '4'):
            num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = self.add(num1, num2)
        elif choice == "2":
            result = self.subtract(num1, num2)
        elif choice == "3":
            result = self.multiply(num1, num2)
        elif choice == "4":
            result = self.divide(num1, num2)
        elif choice == "5":
            exponent = float(input("Enter the exponent: "))
            result = self.power(num1, exponent)
        elif choice == "6":
            result = self.sqrt(num1)
        else:
            result = "Invalid operation."

        print(f"Result: {result}")

if __name__ == "__main__":
    calc = ClassBasedCalculator()
    calc.run_class_based_calculator()
