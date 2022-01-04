import unittest

from ocean import *


class TestSimulationCommands(unittest.TestCase):
    def test_simulator(self):
        for sim in Simulator:
            self.assertEqual(sim, simulator(sim))

    def test_save(self):
        self.assertCountEqual([save_type for save_type in SaveType], save())


if __name__ == '__main__':
    unittest.main()
