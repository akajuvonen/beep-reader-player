import unittest
from note_file_parser import note_file_parser

class NoteFileParserTest(unittest.TestCase):
    """Tests for note parsing from file"""
    def setUp(self):
        filename = 'tests/notefile.txt'
        self.f = open(filename,'r')

    def parse_notes_test(self):
        """Parse notes from a file test"""
        pass
