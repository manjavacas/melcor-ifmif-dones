#!/usr/bin/env python

"""
Optimizacion del caudal rechazado (RJ) en el SGS
"""

import subprocess
import numpy as np

from melkit.toolkit import Toolkit

# Paths
MELGEN_PATH = './melgen-fusion-186_bdba'
MELCOR_PATH = './melcor-fusion-186_bdba'
MODEL_PATH = './SGS-Ar/sgs_final.inp'
EDF_PATH = './SGS_VAR.DAT'

# Presion objetivo
TARGET_PRESSURE = 101065.

# Maxima desviacion de presion permitida
MAX_PRESS_DEVIATION = 40.

# Maximas impurezas permitidas
MAX_IMP_TOTAL = 10.

# Incremento RJ
INC_RJ = 1.


def incorrect_pressure(max_pressure, min_pressure):
    """
    Devuelve True si la presion excede los limites dados.
    """
    overpressure = max_pressure > (TARGET_PRESSURE + MAX_PRESS_DEVIATION)
    underpressure = min_pressure < (TARGET_PRESSURE - MAX_PRESS_DEVIATION)

    return overpressure or underpressure


def imp_exceeded(imps):
    """
    Devuelve True si la concentracion de impurezas total > MAX_IMP
    """
    return imps > MAX_IMP_TOTAL


end = False
toolkit = Toolkit(MODEL_PATH)

while not end:
    # Limpiar entorno y ejecutar MELGEN
    subprocess.call(['make', 'cleanall'],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.call([MELGEN_PATH, MODEL_PATH],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Ejecutar MELCOR
    subprocess.call([MELCOR_PATH, MODEL_PATH],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Leer presiones maximas y ultimas concentraciones del EDF
    with open(EDF_PATH, 'r') as file:
        try:
            df = []
            values = []
            for line in file:
                values.extend([float(value) for value in line.split()])
                if len(values) == 3:
                    df.append(values)
                    values = []
            df = np.array(df)

            max_pressure = np.max(df[:,1], axis=0)
            min_pressure = np.min(df[:,1], axis=0)
            imps = df[-1][2]
        except:
            raise Exception('ERROR en lectura de EDF.')

    # RJ actual
    rj_cf = toolkit.get_cf('CF101')
    rj = float(rj_cf.records['CF10110']['ARADCN_0'])

    # Informacion
    print(''.join(['RJ = ', str(rj),
                   '\n - Max. pressure = ' + str(max_pressure),
                   '\n - Min. pressure = ' + str(min_pressure),
                   '\n - Imps. totales = ' + str(imps),
                   '\n', 90 * '-']))

    # Condiciones
    if incorrect_pressure(max_pressure, min_pressure) or imp_exceeded(imps):
        # Aumentar RJ y actualizar CF
        new_rj = round(rj + INC_RJ, 5)
        rj_cf.update_field('ARADCN_0', new_rj)
        toolkit.remove_comments(overwrite=True)
        toolkit.update_object(rj_cf, overwrite=True)
    else:
        print('\nSOLUCION ENCONTRADA. RJ optimo = ' + str(rj))
        end = True
