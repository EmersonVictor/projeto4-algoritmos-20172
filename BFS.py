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


def bfs(grafo):
    # Realiza um busca em largura em um grafo dado como parâmetro
    marcado = dict()
    for v in grafo.vertices():
        marcado[v] = False

    antecessor = dict()
    for v in grafo.vertices():
        antecessor[v] = -1

    visitar = list()

    for v in grafo.vertices():
        if marcado[v] is False:
            marcado[v] = True
            visitar.append(v)

            while not(visitar == []):
                v = visitar.pop(0)
                for u in grafo.listaAdjacentes(v):
                    if marcado[u] is False:
                        marcado[u] = True
                        antecessor[u] = v
                        visitar.append(u)

    return antecessor
