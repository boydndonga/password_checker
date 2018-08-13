import unittest
import checker


class TestCase(unittest.TestCase):

    def test_functio(self):
        self.assertEqual(checker.validity("arguemet"), False)