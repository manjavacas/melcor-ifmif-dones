#!/usr/bin/python3

import sys

def media_discreta(lista):
    valores_unicos = list(set(lista))
    n = len(lista)

    suma = 0
    for valor in valores_unicos:
        cantidad = lista.count(valor)
        suma += valor * cantidad

    promedio = suma / n
    return promedio

with open(sys.argv[1], "r") as file:
    lines = file.readlines()

import numpy as np

values = list(np.array(lines, dtype=np.float32))

print(media_discreta(values))
