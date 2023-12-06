from Lab1.task10 import main as main_lab1
from Lab2.calc import Calculator
from Lab3.ArtConsole import ArtConsole
from Lab4.CustomArtConsole import CustomArtConsole
from Lab5.main import main as main_lab5
from Lab6.utest import TestCalculator
from Lab7.dogs import main as main_lab7
from Lab8.main import main as main_lab8

import unittest

def choose_program():
    print("Choose a program to run:")
    print("1. Lab1 - Calculator")
    print("2. Lab2 - Calculator (Class-based)")
    print("3. Lab3 - ASCII Art Generator")
    print("4. Lab4 - Custom ASCII Art Generator")
    print("5. Lab5 - 3D ASCII Generator")
    print("6. Lab6 - Unit Test")
    print("7. Lab7 - Dog API Program")
    print("8. Lab8 - Data Visualization")

    choice = input("Enter the number of the program to run: ")

    if choice == "1":
        main_lab1()
    elif choice == "2":
        calc_lab2 = Calculator()
        calc_lab2.run_calculator()
    elif choice == "3":
        console_art = ArtConsole()
        console_art.run()
    elif choice == "4":
        custom_art = CustomArtConsole()
        custom_art.run()
        print(custom_art)
    elif choice == "5":
        main_lab5()
    elif choice == "6":
        unittest.main()
    elif choice == "7":
        main_lab7()
    elif choice == "8":
        main_lab8()
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    choose_program()
