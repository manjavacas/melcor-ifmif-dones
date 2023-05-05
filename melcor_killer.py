#!/usr/bin/python3

import numpy as np
import psutil

with open('VARIABLES.DAT', 'r') as file:
    convergence = False
    while not convergence:
        lines = file.readlines()[-2:]
        
        if len(file.readlines()) > 5:
            line_1 = np.array(lines[0].split(), dtype=np.float32)
            line_2 = np.array(lines[1].split(), dtype=np.float32)

            if ((line_2[1] - line_1[1]) / line_2[1]) < 0.001:
                print('Variacion menor del 0.1%. Deteniendo MELCOR...')
                for proc in psutil.process_iter():
                    try:
                        if proc.name().startswith('melcor'):
                            proc.kill()
                            print(f'El proceso {proc.pid} ha sido finalizado.')
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass
                convergence = True
