#!/usr/bin/python3

from melkit.toolkit import Toolkit

ARGON_INICIAL = 0.98
OXIGENO_INICIAL = round(0.21 * (1. - ARGON_INICIAL), 6)
NITOGRENO_INICIAL = round(0.79 * (1. - ARGON_INICIAL), 6)

PATH = './Main Building/sgs2.inp'

tk = Toolkit(PATH)

cvs = tk.get_cv_list()

for cv in cvs:
    if cv.get_field('NAME') not in ('ENV-IN', 'G-RWTS'):
        cv.update_field('MLFR.8', ARGON_INICIAL)
        cv.update_field('MLFR.5', OXIGENO_INICIAL)
        cv.update_field('MLFR.4', NITOGRENO_INICIAL)
        tk.update_object(cv, overwrite=True)