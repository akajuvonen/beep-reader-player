import unittest
from beep_reader_player import create_melody

class CreateMelodyTest(unittest.TestCase):
    """Test create_melody function"""
    def setUp(self):
        """Set up method for tests."""
        self.bits = 16
        self.sampling_rate = 8000
        self.volumes = [0.5,0.8,1.0]
        self.freqs = [440,440,440]
        self.durations = [0.5,0.5,1.0]
