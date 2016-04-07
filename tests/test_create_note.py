import unittest
from beep_reader_player import create_note

class CreateNoteTest(unittest.TestCase):
    """Test create_note function"""
    def test_create_note(self):
        """Test creating a note"""
        note = create_note(16,8000,1.0,440,1.0)
        # Max and min values for 16 bit int is +-32767
        self.assertEqual(max(note),32767.0)
        self.assertEqual(min(note),-32767.0)
        # Length should be same as sampling rate
        self.assertEqual(len(note),8000)

    def test_volume(self):
        """Max volume always between 0 and 1"""
        # Volume less than 0
        volume = -2.0
        note = create_note(16,8000,volume,440,1.0)
        # Make sure values correct
        self.assertEqual(max(note),0.0)
        # Volume over 1
        volume = 12.0
        note = create_note(16,8000,volume,440,1.0)
        # Make sure max value still correct
        self.assertEqual(max(note),32767.0)
