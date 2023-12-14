import unittest
from Labs.Classes.Lab2.ClassBasedCalc import ClassBasedCalculator

class TestClassBasedCalculator(unittest.TestCase):
    def setUp(self):
        # Ініціалізація калькулятора перед кожним тестом
        self.calc = ClassBasedCalculator()

    def test_add(self):
        # Перевірка, чи додається два числа правильно
        result = self.calc.add(150, 50)
        self.assertEqual(result, 200)

    def test_subtract(self):
        # Перевірка, чи відбувається віднімання правильно
        result = self.calc.subtract(17, 5)
        self.assertEqual(result, 12)

    def test_multiply(self):
        # Перевірка, чи множення працює правильно
        result = self.calc.multiply(10, 10)
        self.assertEqual(result, 100)

    def test_divide(self):
        # Перевірка, чи ділення працює правильно
        result = self.calc.divide(333, 3)
        self.assertEqual(result, 111)

    def test_add_negative(self):
        # Перевірка, чи додається від'ємне число правильно
        result = self.calc.add(-150, 50)
        self.assertEqual(result, -100)

    def test_power(self):
        # Перевірка, чи піднесення до ступеня працює правильно
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)

    def test_sqrt(self):
        # Перевірка, чи корінь квадратний обчислюється правильно
        result = self.calc.sqrt(25)
        self.assertEqual(result, 5)

    def test_sqrt_negative(self):
        # Перевірка, чи виникає виняток, якщо корінь від'ємного числа
        with self.assertRaises(ValueError):
            self.calc.sqrt(-25)

    def run_tests(self):
        # Запуск всіх тестів
        unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(self.__class__))

if __name__ == '__main__':
    # Запуск тестів при запуску файла
    test_runner = TestClassBasedCalculator()
    test_runner.run_tests()
