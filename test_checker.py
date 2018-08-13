import unittest
import checker


class TestCase(unittest.TestCase):

    def test_password_length(self):
        self.assertEqual(checker.validity("argu"), False)

    def test_special_characters(self):
        self.assertEqual(checker.validity("argu@$#"), True)