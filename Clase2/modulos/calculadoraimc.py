# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:21:57 2022

@author: kapon
"""

class PesoValueError(Exception):
    """error al ingresar valor negativo"""

class AlturaValueError(Exception):
    """error al ingresar valor negativo"""



class CalculadoraIMC:
    def __init__ (self, altura, peso):
        self.peso=peso
        self.altura=altura
        self.imc = 0
            
    @property
    def peso(self):
        return self._peso
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        if altura <= 0:
            raise AlturaValueError("la altura no peude ser negativa")
        else:
            self._altura = altura
    
    @peso.setter
    def peso(self, peso):
        if peso <= 0:
            raise PesoValueError("El peos no puede ser negativo")
        else:
            self._peso = peso
            
    @property
    def calcular_imc(self):
        self.imc = round(self.peso/(self.altura**2),2)
        return self.imc
        
    @property
    def mostrar(self):
        if self.imc < 18.5:
            print(f'Tu IMC {self.imc} esta debajo de lo normal')
        elif self.imc <25:
            print(f'Tu IMC {self.imc} es normal')
        elif self.imc < 30:
            print(f'Tu IMC {self.imc} indica sobrepeso')
        else:
            print(f'Tu IMC {self.imc} indica obecidad')
        

if __name__ == '__main__':
    peso = input('ingrese peso: ')
    altura = input('ingrese altura: ')
    imc = CalculadoraIMC(float(altura), float(peso))
    imc.calcular_imc
    imc.mostrar
    
    
    
    
