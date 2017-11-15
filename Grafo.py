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

    def direcionado(self):
        # Devolve um valor booleano que representa se o grafo é direcionado ou não
        return self.__direcionado

    def criarGrafo(self, listaVertices):
        # Criar grafo com v vértices e sem arestas
        for v in listaVertices:
            self.__listaAdj[v] = list()

    def inserirAresta(self, verticeOrigem, verticeDestino):
        # Inserir aresta de um vértice origem para um vértice destino
        if verticeOrigem in self.__listaAdj and verticeDestino in self.__listaAdj:
            if self.direcionado() is True:
                self.__listaAdj[verticeOrigem].append(verticeDestino)
            else:
                self.__listaAdj[verticeOrigem].append(verticeDestino)
                self.__listaAdj[verticeDestino].append(verticeOrigem)
        else:
            raise KeyError("Grafo não possui vértice de origem ou vértice de destino")

    def verificarAresta(self, verticeOrigem, verticeDestino):
        # Verificar se aresta entre vértice de origem e vértice destino existe
        if verticeOrigem in self.__listaAdj and verticeDestino in self.__listaAdj:
            if verticeDestino in self.__listaAdj[verticeOrigem]:
                return True
            else:
                return False
        else:
            raise KeyError("Grafo não possui vértice de origem ou vértice de destino")

    def listaAdjacentes(self, vertice):
        # Devolve a lista de vértices adjancentes a um vértice
        if vertice in self.__listaAdj:
            return self.__listaAdj[vertice]
        else:
            raise KeyError("Grafo não possui vertice")

    def removerAresta(self, verticeOrigem, verticeDestino):
        # Remover uma aresta entre v[értice origem e vértice destino
        if verticeOrigem in self.__listaAdj and verticeDestino in self.__listaAdj:
            if self.direcionado() is True:
                self.__listaAdj[verticeOrigem].remove(verticeDestino)
            else:
                self.__listaAdj[verticeOrigem].remove(verticeDestino)
                self.__listaAdj[verticeDestino].remove(verticeOrigem)
        else:
            raise KeyError("Grafo não possui vértice de origem ou vértice de destino")

    def numVertices(self):
        # Número de vértices do grafo
        return len(self.__listaAdj)

    def numArestas(self):
        # Número de arestas do grafo
        arestas = 0
        for v in self.__listaAdj:
            arestas += len(self.__listaAdj[v])

        if self.direcionado() is True:
            return arestas
        else:
            return arestas // 2

    def vertices(self):
        # Devolve todos os vertices do grafo
        return [v for v in self.__listaAdj]

    def imprimirGrafo(self):
        # Imprimir grafo
        for v in self.__listaAdj:
            representacao = "Vértice: {0} --> Adjancentes: {1}".format(v,self.__listaAdj[v])
            print(representacao)
