#!/usr/bin/python3

"""
Optimizacion del caudal rechazado (RJ) en el SGS
"""

import subprocess
import numpy as np

from melkit.toolkit import Toolkit

# Paths
MELGEN_PATH = './melgen-fusion-186_bdba'
MELCOR_PATH = './melcor-fusion-186_bdba'
MODEL_PATH = './main-building/sgs3.inp'
EDF_PATH = './SGS_VAR.DAT'

# Presion objetivo
TARGET_PRESSURE = 101065.

# Maxima desviacion de presion permitida
MAX_PRESS_DEVIATION = 40

# Maximas impurezas permitidas
MAX_IMP_O2 = .5
MAX_IMP_N2 = .5
MAX_IMP_H2O = .1

# Incremento RJ
INC_RJ = .00001


def overpressure(pressures):
    """
    Devuelve True si alguna presion > TARGET_PRESSURE + MAX_PRESS_DEVIATION
    """
    return any(value > (TARGET_PRESSURE + MAX_PRESS_DEVIATION) for value in pressures)


def imp_exceeded(imps_o2, imps_n2, imps_h2o):
    """
    Devuelve True si alguna concentracion > MAX_IMP_x
    """
    o2_exceeded = any(value > MAX_IMP_O2 for value in imps_o2)
    n2_exceeded = any(value > MAX_IMP_N2 for value in imps_n2)
    h2o_exceeded = any(value > MAX_IMP_H2O for value in imps_h2o)

    return o2_exceeded or n2_exceeded or h2o_exceeded


end = False

# Obtener RJ inicial
toolkit = Toolkit(MODEL_PATH)
rj_cf = toolkit.get_cf('CF101')

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
                if len(values) == 17:
                    df.append(values)
                    values = []
            df = np.array(df)

            imps_o2 = df[-1][5:9]
            imps_n2 = df[-1][9:13]
            imps_h2o = df[-1][13:17]
            max_pressures = np.max(df[:, 1:5], axis=0)
        except:
            raise Exception('ERROR en lectura de EDF.')

    # Informacion
    rj = float(rj_cf.records['CF10110']['ARADCN_0'])
    print(''.join(['RJ = ', str(rj),
                   '\n - Max. pressures = ', str(max_pressures),
                   '\n - Imps. O2 = ', str(imps_o2),
                   '\n - Imps. N2 = ', str(imps_n2),
                   '\n - Imps. H2O = ', str(imps_h2o),
                   '\n', 90 * '-']))

    # Condiciones
    if overpressure(max_pressures) or imp_exceeded(imps_o2, imps_n2, imps_h2o):
        # Aumentar RJ y actualizar CF
        new_rj = round(rj + INC_RJ, 5)
        rj_cf.update_field('ARADCN_0', new_rj)
        toolkit.remove_comments(overwrite=True)
        toolkit.update_object(rj_cf, overwrite=True)
    else:
        print('\nSOLUCION ENCONTRADA. RJ optimo = ' + str(rj))
        end = True
