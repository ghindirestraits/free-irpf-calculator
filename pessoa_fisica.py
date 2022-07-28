#!/bin/env/python3

"""
    Implementação da classe PessoaFisica

    Atributos:
        - Privados:
        - Públicos:
    
    Métodos:
        - Privados:
        - Públicos:
"""

class PessoaFisica():
    def __init__(self, nome:str, cpf:int, totalRendimentos:int = 0, despesas:int = 0) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__totalRends = totalRendimentos
        self.__despesas = despesas
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novoNome: str):
        self.__nome = novoNome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novoCpf:int):
        self.__cpf = novoCpf
