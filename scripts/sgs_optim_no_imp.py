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
MODEL_PATH = './sgs_final_copy.inp'
EDF_PATH = './sgs_var.DAT'

# Presion objetivo
TARGET_PRESSURE = 101065.

# Maxima desviacion de presion permitida
MAX_PRESS_DEVIATION = 40

# Incremento RJ
INC_RJ = .1

def bad_pressure(max_pressures, min_pressures):
    """
    Devuelve True si alguna presion no esta en el rango +-40
    """
    press_cond_1 = any(value < (TARGET_PRESSURE - MAX_PRESS_DEVIATION)
                       for value in min_pressures)
    press_cond_2 = any(value > (TARGET_PRESSURE + MAX_PRESS_DEVIATION)
                       for value in max_pressures)

    return press_cond_1 or press_cond_2


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

    # Leer presiones maximas
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
            max_pressures = np.max(df[:, 1:5], axis=0)
            min_pressures = np.min(df[:, 1:5], axis=0)
        except:
            raise Exception('ERROR en lectura de EDF.')

    # RJ actual
    rj_cf = toolkit.get_cf('CF101')
    rj = float(rj_cf.records['CF10110']['ARADCN_0'])

    # Informacion
    print(''.join(['RJ = ', str(rj),
                   '\n - Max. pressures = ', str(max_pressures),
                   '\n - Min. pressures = ', str(min_pressures),
                   '\n', 90 * '-']))

    # Condiciones
    if bad_pressure(max_pressures, min_pressures):
        # Aumentar RJ y actualizar CF
        new_rj = round(rj + INC_RJ, 5)
        rj_cf.update_field('ARADCN_0', new_rj)
        toolkit.remove_comments(overwrite=True)
        toolkit.update_object(rj_cf, overwrite=True)
    else:
        print('\nSOLUCION ENCONTRADA. RJ optimo = ' + str(rj))
        end = True
