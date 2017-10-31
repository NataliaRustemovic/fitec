import unittest


def is_divisible(number, divisor):
    return number % divisor == 0


def foobarqix(number):
    if is_divisible(number, 3):
        return "Foo"
    else:
        return "Bar"


class FooBarQixTestCase(unittest.TestCase):
    def test_return_Foo_when_number_is_devisible_by_3(self):
        self.assertEqual(foobarqix(3), "Foo")

    def test_return_Bar_when_number_is_devisible_by_5(self):
        self.assertEqual(foobarqix(5), "Bar")


unittest.main()
