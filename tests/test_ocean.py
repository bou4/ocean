import unittest

from ocean import *

class TestSimulationCommands(unittest.TestCase):
    def test_simulator(self):
        for sim in Simulator:
            self.assertEqual(sim, simulator(sim))


if __name__ == '__main__':
    unittest.main()
