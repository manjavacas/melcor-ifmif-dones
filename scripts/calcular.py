#!/usr/bin/env python3

'''
Script con cálculos básicos para validación de fugas
'''

from math import pi, sqrt

R = 8.314466185324

HLRS = {'C1': 10e-01, 'C2': 10e-02, 'C3': 2.5*10e-03, 'C4': 5*10e-04}


def calcular_dh_circular():
    '''
    DH = 4A / P; P = 2piR; R = sqrt(a/pi)
    '''

    a = float(input('Introducir área de paso (m2): '))
    return (4 * a) / (2 * pi * sqrt(a / pi))


def calcular_dh_cuadrado():
    '''
    DH = 4A / P; P = 4xy
    '''

    y = float(input('Introducir altura (m2): '))
    x = float(input('Introducir ancho (m2): '))
    return (4 * y * x) / (2 * x + 2 * y)


def oxygen_method():
    '''
    Basado en informe sobre validacion de fugas: shorturl.at/fPRWX
    '''

    V = float(input('Introducir volumen de la sala:'))
    m = float(input('Introducir masa final de O2 (Kg): '))
    T = float(input('Introducir temperatura final (K): '))
    P = float(input('Introducir presión final (Pa): '))
    t = float(input('Introducir tiempo de simulación (seg): '))

    C = (234375 * R) / (14 * V)
    X = (pow(m, 2) * T) / (P * t)

    hlr = C * X
    print('Hourly leak rate = ', hlr)

    clase = input('Introducir clase (C4, C3, C2, C1): ')
    if hlr < HLRS[clase]:
        print(f'Fuga válida: {hlr} < {HLRS[clase]}')
    else:
        print(f'Fuga no válida: {hlr} >= {HLRS[clase]}')


if __name__ == '__main__':
    op = int(input(
        'Introducir opción:\n [1] Calcular diámetro hidraúlico FL circular\n [2] Calcular diámetro hidráulico FL cuadrado\n [3] Oxygen method\n'))
    if op == 1:
        dh = calcular_dh_circular()
        print('Diámetro hidráulico: ', dh)
    elif op == 2:
        dh = calcular_dh_cuadrado()
        print('Diámetro hidráulico: ', dh)
    elif op == 3:
        oxygen_method()
    else:
        print('Opción incorrecta')
        exit()
