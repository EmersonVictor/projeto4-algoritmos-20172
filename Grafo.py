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

    def __repr__(self):
        return str(self.__listaAdj)

    def criarGrafo(self, listaVertices):
        # Criar grafo com v vértices e sem arestas
        for v in listaVertices:
            self.__listaAdj[v] = list()

    def inserirAresta(self, verticeOrigem, verticeDestino):
        # Inserir aresta de um vertice origem para um vertice destino
        if verticeOrigem in self.__listaAdj and verticeDestino in self.__listaAdj:
            if self.__direcionado is True:
                self.__listaAdj[verticeOrigem].append(verticeDestino)
            else:
                self.__listaAdj[verticeOrigem].append(verticeDestino)
                self.__listaAdj[verticeDestino].append(verticeOrigem)
        else:
            raise KeyError("Grafo não possui vertice de origem ou vertice de destino")

    def verificarAresta(self, verticeOrigem, verticeDestino):
        # Verificar se aresta entre vertice de origem e vertice destino existe
        if verticeOrigem in self.__listaAdj and verticeDestino in self.__listaAdj:
            if verticeDestino in self.__listaAdj[verticeOrigem]:
                return True
            else:
                return False
        else:
            raise KeyError("Grafo não possui vertice de origem ou vertice de destino")

    def listaAdjacentes(self, vertice):
        # Devolve a lista de vertices adjancentes a um vertice
        if vertice in self.__listaAdj:
            return self.__listaAdj[vertice]
        else:
            raise KeyError("Grafo não possui vertice")

    def removerAresta(self, verticeOrigem, verticeDestino):
        # Remover uma aresta entre vertice origem e vertice destino
        if verticeOrigem in self.__listaAdj and verticeDestino in self.__listaAdj:
            if self.__direcionado is True:
                self.__listaAdj[verticeOrigem].remove(verticeDestino)
            else:
                self.__listaAdj[verticeOrigem].remove(verticeDestino)
                self.__listaAdj[verticeDestino].remove(verticeOrigem)
        else:
            raise KeyError("Grafo não possui vertice de origem ou vertice de destino")

    def imprimirGrafo():
        pass

    def numVertices():
        pass

    def numAresta():
        pass

    def direcionado():
        pass


if __name__ == "__main__":
    a = Grafo(True)
    print(a)

    a.criarGrafo([1, 2, 3, 4])
    print(a)

    a.inserirAresta(2, 4)
    print(a)
    a.inserirAresta(2, 3)
    print(a)
    a.inserirAresta(2, 1)
    print(a)

    print(a.verificarAresta(2,4))
    print(a.verificarAresta(4,3))

    print(a.listaAdjacentes(2))
