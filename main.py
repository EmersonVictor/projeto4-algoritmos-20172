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

from Grafo import Grafo
from BFS import bfs
import timeit


def tempoCriacao(arquivo):
    # Calcula o tempo de criação de um grafo a partir de um arquivo
    arquivo = open(arquivo, "r")
    infoGrafo = arquivo.readline()
    infoGrafo = infoGrafo.split()

    if infoGrafo[1] == "sym" and infoGrafo[2] == "unweighted":
        grafo = Grafo(False, False)

    elif infoGrafo[1] == "asym" and infoGrafo[2] == "posweighted":
        grafo = Grafo(True, True)

    elif infoGrafo[1] == "asym" and infoGrafo[2] == "unweighted":
        grafo = Grafo(True, False)

    elif infoGrafo[1] == "sym" and infoGrafo[2] == "posweighted":
        grafo = Grafo(False, True)

    listaArestas = [linha.split() for linha in infoGrafo.readlines()]
    start = timeit.default_timer()

    if grafo.ponderado():
        for aresta in listaArestas:
            grafo.inserirAresta(aresta[1], aresta[2], aresta[3])
    else:
        for aresta in listaArestas:
            grafo.inserirAresta(aresta[1], aresta[2])

    end = timeit.default_timer()
    return grafo, end - start


def tempoBusca(grafo):
    start = timeit.default_timer()
    antecessores = bfs(grafo)
    end = timeit.default_timer()

    return antecessores, end - start

    # Calcula o tempo de criação de um grafo a partir de um arquivo


def main():
    arquivos = ["/grafos_teste/airTrafficControl.txt",
                "/grafos_teste/chicago.txt",
                "/grafos_teste/dolphins.txt",
                "/grafos_teste/euroroad.txt",
                "/grafos_teste/facebook.txt",
                "/grafos_teste/linux.txt",
                "/grafos_teste/usairport.txt"]

    resultados = open("resultados.txt", "a+")

    for arq in arquivos:
        grafo, criacao = tempoCriacao(arq)
        antecessores, busca = tempoBusca(grafo)

        resultados.write("Grafo 1 \n Tempo de criação: {0} \n Tempo de busca: {1} \n Antecessores: {2}".format(criacao, busca, antecessores))

    resultados.close()


if __name__ == '__main__':
    teste = open("chicago.txt", "r")
    a, b = tempoCriacao(teste)
    c, d = tempoBusca(a)
    print(a, b, c, d)
