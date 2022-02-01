# pylint: disable=missing-docstring
import unittest

from parameterized import parameterized

from src.multiply.calculator import Calculator


class TestCalculator(unittest.TestCase):
    @parameterized.expand([
        (2, 1),
        (2, 2),
        (3, 5),
        (5, 3),
    ])
    def test_multiply(self, operand_1, operand_2):
        self.assertEqual(Calculator.multiply(operand_1, operand_2), operand_1 * operand_2)
