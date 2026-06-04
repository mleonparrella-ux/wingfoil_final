# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:39:49 2026

@author: usuario
"""

def validar_viento(viento):

    try:
        viento = float(viento)

        if viento <= 0:
            return False

        return True

    except:
        return False


def validar_sensacion(sensacion):

    try:
        sensacion = int(sensacion)

        return 1 <= sensacion <= 10

    except:
        return False