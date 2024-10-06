import unittest

def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed"
    else:
        return "Invalid operation"

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator(5, 3, 'add'), 8)

    def test_subtract(self):
        self.assertEqual(calculator(10, 5, 'subtract'), 5)

    def test_multiply(self):
        self.assertEqual(calculator(6, 4, 'multiply'), 24)

    def test_divide(self):
        self.assertEqual(calculator(9, 3, 'divide'), 3.0)

    def test_divide_by_zero(self):
        self.assertEqual(calculator(10, 0, 'divide'), "Error: Division by zero is not allowed")

    def test_negative_addition(self):
        self.assertEqual(calculator(-5, -3, 'add'), -8)

    def test_subtract_negative(self):
        self.assertEqual(calculator(7, -2, 'subtract'), 9)

    def test_multiply_by_zero(self):
        self.assertEqual(calculator(0, 9, 'multiply'), 0)

    def test_invalid_operation(self):
        self.assertEqual(calculator(15, 5, 'unknown'), "Invalid operation")

    def test_add_floats(self):
        self.assertEqual(calculator(8.5, 2.5, 'add'), 11.0)

if __name__ == '__main__':
    unittest.main()