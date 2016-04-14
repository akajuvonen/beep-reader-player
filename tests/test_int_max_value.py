import unittest
from beep_reader_player import int_max_value

class IntMaxTest(unittest.TestCase):
    def setUp(self):
        self.bits = 16
        self.signed_expected_max = 32767
        self.unsigned_expected_max = 65535

    def test_int_max_value_signed(self):
        signed = True
        max_value = int_max_value(self.bits,signed)
        self.assertEqual(max_value,self.signed_expected_max)

    def test_int_max_value_unsigned(self):
        signed = False
        max_value = int_max_value(self.bits,signed)
        self.assertEqual(max_value,self.unsigned_expected_max)
