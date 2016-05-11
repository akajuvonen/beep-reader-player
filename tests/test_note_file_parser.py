import unittest
from note_file_parser import note_file_parser

class NoteFileParserTest(unittest.TestCase):
    """Tests for note parsing from file"""
    def parse_notes_test(self):
        """Parse notes from a file test"""
        notes,durations = note_file_parser('tests/notefile.txt')
        self.assertEqual(notes,['C4','D4','E4'])
        self.assertEqual(durations,[1.0,1.0,1.0])
