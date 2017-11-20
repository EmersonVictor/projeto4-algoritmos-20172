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
    grafoArquivo = open(arquivo, "r")
    infoGrafo = grafoArquivo.readline()
    infoGrafo = infoGrafo.split()

    if infoGrafo[1] == "sym" and infoGrafo[2] == "unweighted":
        grafo = Grafo(False, False)

    elif infoGrafo[1] == "asym" and infoGrafo[2] == "posweighted":
        grafo = Grafo(True, True)

    elif infoGrafo[1] == "asym" and infoGrafo[2] == "unweighted":
        grafo = Grafo(True, False)

    elif infoGrafo[1] == "sym" and infoGrafo[2] == "posweighted":
        grafo = Grafo(False, True)

    listaArestas = [linha.split() for linha in grafoArquivo.readlines()]
    grafoArquivo.close()

    start = timeit.default_timer()
    if grafo.ponderado():
        for aresta in listaArestas:
            grafo.inserirAresta(int(aresta[0]), int(aresta[1]), int(aresta[2]))
    else:
        for aresta in listaArestas:
            grafo.inserirAresta(int(aresta[0]), int(aresta[1]))

    end = timeit.default_timer()
    return grafo, end - start


def tempoBusca(grafo):
    start = timeit.default_timer()
    antecessores = bfs(grafo)
    end = timeit.default_timer()

    return antecessores, end - start

    # Calcula o tempo de criação de um grafo a partir de um arquivo


def main():
    arquivos = ["airTrafficControl.txt",
                "chicago.txt",
                "dolphins.txt",
                "euroroad.txt",
                "facebook.txt",
                "linux.txt",
                "usairport.txt"]

    resultados = open("resultados.txt", "a+")

    for arq in arquivos:
        grafo, criacao = tempoCriacao(arq)
        antecessores, busca = tempoBusca(grafo)


        resultados.write("Grafo {3} \n Tempo de criação: {0} \n Tempo de busca: {1} \n Antecessores: {2}\n\n".format(criacao, busca, antecessores, arq))

    resultados.close()


if __name__ == '__main__':
    main()
