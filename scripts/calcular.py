#!/usr/bin/env python3

'''
Script con cálculos básicos para validación de fugas
'''

from math import pi, sqrt

PESO_MOL_O2 = 32  # gramos
R = 8.314472
P = 100364.23
T = 292.98

HLRS = {'C1': 10e-01, 'C2': 10e-02, 'C3': 2.5*10e-03, 'C4': 5*10e-04}


def calcular_dh_circular():
    # DH = 4A / P; P = 2piR; R = sqrt(a/pi)
    a = float(input('Introducir área de paso (m2): '))
    return (4 * a) / (2 * pi * sqrt(a / pi))


def calcular_dh_cuadrado():
    # DH = 4A / P; P = 4xy
    y = float(input('Introducir altura (m2)'))
    x = float(input('Introducir ancho (m2): '))
    return (4 * y * x) / (2 * x + 2 * y)


def oxygen_method():
    t = float(input('- Introducir tiempo de simulación (seg): '))
    t0 = float(input('- Introducir temperatura inicial (K): ')) - \
        273.15  # conversion a celsius
    t1 = float(input('- Introducir temperatura final (K): ')) - \
        273.15  # conversion a celsius
    p0 = float(input('- Introducir presión inicial (Pa): '))
    p1 = float(input('- Introducir presión final (Pa): '))

    if abs(t1 - t0) > 3:
        print('[!] No se cumple la condición: |t1 - t0| < 3ºC')
        exit()
    elif abs(p1 - p0) > 50:
        print('[!] No se cumple la condición: |p1 - p0| < 50')
        exit()
    else:
        print('\n ** Se cumplen las condiciones de presión y temperatura. ** \n')

        # Conversion de O2 a moles
        masa_o2_final = float(
            input('- Introducir masa de O2 en timestep final (Kg): '))
        n = (masa_o2_final * 1e+03) / PESO_MOL_O2

        # Calculo del volumen molar
        V = (n * R * T) / P
        vol_sala = float(input('- Introducir volumen de la sala (m3): '))
        vpm = ((V / PESO_MOL_O2) * (masa_o2_final * 1e+06)) / vol_sala

        # Hourly leak rate
        hourly_leak_rate = 300 * vpm / ((t / 60) * 1e+06)

        clase = input(
            '- Introducir clase del volumen de control SEGÚN ISO 17873 (C4, C3, C2, C1): ')
        if clase not in ['C1', 'C2', 'C3', 'C4']:
            print('[!] Clase incorrecta. Debe ser C1, C2, C3 o C4.')
            exit()

        if hourly_leak_rate < HLRS[clase]:
            print(
                f'\n** Cumple con la ISO. Hourly leak rate = {hourly_leak_rate} < {HLRS[clase]} **\n')
        else:
            print(
                f'\n** No cumple con la ISO. Hourly leak rate = {hourly_leak_rate} >= {HLRS[clase]} **\n')


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
