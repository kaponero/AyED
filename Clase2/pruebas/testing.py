# -*- coding: utf-8 -*-

from modulos.calculadoraimc import CalculadoraIMC, PesoValueError, AlturaValueError
import unittest

class TestCalculoIMC(unittest.TestCase):
    
    def setUp(self):
        self.imc1 = CalculadoraIMC(1.73,71)
    def test_IMC(self):
        imc2 = CalculadoraIMC(1.73,71)
        self.assertEqual(imc2.calcular_imc,23.72)
    
    def test_excepcionPeso(self):
        with self.assertRaises(PesoValueError):
            self.imc1.peso = -5
    
    def test_excepcionAltura(self):
        with self.assertRaises(AlturaValueError):
            self.imc1.altura = -5


if __name__ == '__main__':
    unittest.main()