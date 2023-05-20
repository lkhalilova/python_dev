import unittest


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


class TestSymbolCheck(unittest.TestCase):
    def test_factorial(self):
        n = 3
        self.assertEqual(factorial(n), 6)

    def test_incorrect_type(self):
        with self.assertRaises(TypeError):
            factorial("Text")


if __name__ == "__main__":
    unittest.main()


