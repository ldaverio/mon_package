import unittest

from mon_package import Boat


class BoatTests(unittest.TestCase):

    def test_nom(self):
        b = Boat('O mon batôô')
        self.assertEqual(b.nom, 'O mon batôô')

