# -*- coding: utf-8 -*-
'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF969 - Algoritmos e estrutura de dados

Autor:  Emerson Victor Ferreira da Luz (evfl)
Email:  evfl@cin.ufpe.br
Data:   2017-10-22

Copyright(c) 2017 Emerson Victor
'''


class Grafo:
    '''Classe grafo é uma representação abstrata de um grafo,
    implementada por meio de lista de adjacências'''
    def __init__(self, direcionado):
        self.__listaAdj = dict()
        self.__direcionado = direcionado

    def criarGrafo(self, listaVertices):
        # Criar grafo com v vértices e sem arestas
        for v in listaVertices:
            self.__listaAdj[v] = list()

    def inserirAresta(self, verticeOrigem, verticeDestino):
        # Inserir aresta de um vertie origem para um vertice destino
        for v in self.__listaAdj:
            if v == verticeOrigem:
                self.__listaAdj[v].append(verticeDestino)

    def verificarAresta():
        pass

    def listaAdjacentes():
        pass

    def removerAresta():
        pass

    def imprimirGrafo():
        pass

    def numVertices():
        pass

    def numAresta():
        pass

    def direcionado():
        pass
