import unittest


def is_divisible(number, divisor):
    return number % divisor == 0


def foobarqix(number):
    result = ""
    if is_divisible(number, 3):
        result += "Foo"
    if is_divisible(number, 5):
        result += "Bar"
    if is_divisible(number, 7):
        result += "Qix"
    if result != "":
        return result
    else:
        return "1"


class FooBarQixTestCase(unittest.TestCase):
    def test_return_Foo_when_number_is_devisible_by_3(self):
        self.assertEqual(foobarqix(3), "Foo")

    def test_return_Bar_when_number_is_devisible_by_5(self):
        self.assertEqual(foobarqix(5), "Bar")

    def test_return_Qix_when_number_is_devisible_by_7(self):
        self.assertEqual(foobarqix(7), "Qix")

    def test_return_FooBar_when_number_is_devisible_by_3_and_5(self):
        self.assertEqual(foobarqix(15), "FooBar")

    def test_return_1_when_number_is_1(self):
        self.assertEqual (foobarqix(1), "1")

unittest.main()
