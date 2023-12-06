import unittest
from Lab2.calc import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    #Операція додавання
    def test_add(self):
        calc = Calculator()
        result = calc.add(150, 50)
        self.assertEqual(result, 200)

    #Операція віднімання
    def test_subtr(self):
        calc = Calculator()
        result = calc.subtract(17, 5)
        self.assertEqual(result, 12)


    #Операція множення
    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(10, 10)
        self.assertEqual(result, 100)

    #Операція ділення
    def test_divide(self):
        calc = Calculator()
        result = calc.divide(333, 3)
        self.assertEqual(result, 111)

    #Перевірка коректності ділення на нуль
    def test_divide_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.divide(100, 0)

    #Операція додавання з від'ємними операндами
    def test_add_negative(self):
        calc = Calculator()
        result = calc.add(-150, 50)
        self.assertEqual(result, -100)

    # Тести для операції ділення на нуль
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError, msg="Помилка: Ділення на нуль неможливе."): #Якщо при діленні на нуль програма калькулятора видає помилку, то тест вважається успішним.
            self.calc.divide(100, 0)


    def test_invalid_input(self):
        with self.assertRaises(ValueError, msg="Помилка: Введене значення має бути числом."): # Якщо при введенні некоректного символа в операції програма видає помилку, то тест вважається успішним.
            self.calc.perform_calculation(float('word'), '+', 5)


if __name__ == '__main__':
    unittest.main()
