import random

def distance_crash_point(plateau,zone_objectif,zone_crash):

    return 0

def evaluation(dict_global):
    variables_fin = dict_global[len(dict_global)-2]
    plateau = dict_global['plateau']
    if variables_fin['Y'] < plateau[int(variables_fin['X'])]:
        distance_altitude_point = 0
    else:
        distance_altitude_point = abs(plateau[variables_fin['X']] - variables_fin['Y'])
    #créer une fonction pour trouver le début et la fin de la zone d'aterissage par rapport au tableau plateau
    zone_atterissage_debut = 2000
    zone_atterissage_fin = 3500
    distance_zone_aterrisage_debut = distance_crash_point(plateau,zone_atterissage_debut,variables_fin['Y'])
    variables_fin['hSpeed'] = -50
    variables_fin['fuel'] = 1000
    variables_fin['rotate'] = 90
    print()

def newSimulation(save_try):
    new_rotate = random.randint(-90,90)
    new_power = random.randint(0,4)
    return new_rotate,new_power