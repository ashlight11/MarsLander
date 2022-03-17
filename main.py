import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from affichage import affichage,construction_plateau

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import scipy
from scipy import integrate



def next_periode(attributs, periode_actuelle):
    periode_suivante = periode_actuelle + attribution(attributs)
    return periode_suivante


def attribution(anciens_attributs):
    nouveaux_attributs = 0
    # truc aléatoire d'apprentissage
    if contraintes_attribution(anciens_attributs, nouveaux_attributs):
        return nouveaux_attributs
    else:
        attribution(anciens_attributs)


def contraintes_attribution(anciens, nouveaux):
    if np.abs(np.abs(anciens['rotate']) - np.abs(anciens['rotate'])) > 15 or np.abs(
            np.abs(anciens['power']) - np.abs(anciens['power'])) > 1:
        return False
    else:
        return True





def find_landing_area(ground):
    begin_flat = 0
    end_flat = 0
    for index, element in enumerate(ground):
        if index != len(ground) - 1 and element[1] == ground[index + 1][1]:
            begin_flat = element
            end_flat = ground[index + 1]

    return begin_flat, end_flat




def __main__():
    data = initialisation()
    affichage(data,0,0,0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    __main__()