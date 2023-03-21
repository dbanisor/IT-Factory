from sesiune_8.Tema_8.app.tema_7 import FormaGeometrica, Patrat, Cerc
import unittest
import pytest
from abc import ABC, abstractmethod
from parameterized import parameterized
'''
1. Alegeti 3 functii din cele implementate la tema anterior,
si scrieti unit tests pentru ele folosind unittest.
'''

# class TestPatratCerc(unittest.TestCase):
#     def setUp(self) -> None:
#         self.p = Patrat(4)
#         self.c = Cerc(5)
#
#     def test_patrat_aria(self):
#         self.assertEqual(16, self.p.aria())
#
#     def test_cerc_aria(self):
#         self.assertEqual(78.5, self.c.aria())
#
#     def test_cerc_descrie(self):
#         self.assertEqual(None, self.c.descrie())

'''
3. Alegeti una din temele de mai sus, 
si convertiti testele din unittest in pytest
'''

#
# def test_patrat_aria():
#     p = Patrat(4)
#     assert p.aria() == 16
#
# def test_cerc_aria():
#     c = Cerc(5)
#     assert c.aria() == 78.5

'''
4. Folosind TDD, rezolvati urmatoarea problema: Sa se scrie o ierarhie de clase 
pentru forme geometrice: FormaGeometrica, Patrat, Dreptunghi, Cerc. 
FormaGeometrica este interfata, adica clasa abstracta cu doar metode astracte. 
Metode: arie(), perimetru(). Sa se mosteneasca interfata, si sa se implementeze 
cele 2 metode pentru fiecare din cele 3 forme geometrice.
'''

class TestPatrat(unittest.TestCase):

    @parameterized.expand([
        (Patrat(4), 16),
        (Patrat(5), 25),
        (Patrat(9), 81)
    ])
    def test_aria(self, patrat, expected):
        self.assertEqual(patrat.aria(), expected)

    @parameterized.expand([
        (Patrat(3), 12),
        (Patrat(5), 20),
        (Patrat(9), 36)
    ])
    def test_perimetru(self, patrat, expected):
        self.assertEqual(patrat.perimetru(), expected)

class TestCerc(unittest.TestCase):

    @parameterized.expand([
        (Cerc(4), 50.27),
        (Cerc(5), 78.54),
        (Cerc(9), 254.47)
    ])
    def test_aria(self, cerc, expected):
        self.assertEqual(cerc.aria(), expected)

    @parameterized.expand([
        (Cerc(3), 18.85),
        (Cerc(5), 31.42),
        (Cerc(9), 56.55)
    ])
    def test_perimetru(self, cerc, expected):
        self.assertEqual(cerc.perimetru(), expected)
