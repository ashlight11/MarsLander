import random
import numpy as np
import atterissage as att

from MarsLanderSim import MarsLanderSim


def evaluation(dict_global):
    variables_fin = dict_global[len(dict_global) - 2]
    plateau = dict_global['plateau']

    coordonnee = plateau[0]
    coordonnee = np.array(coordonnee)
    var = np.where(coordonnee == int(variables_fin['X']))
    if variables_fin['Y'] < plateau[1][var[0][0]]:
        distance_altitude_point = 0
    else:
        distance_altitude_point = abs(plateau[1][var[0][0]] - variables_fin['Y'])
    # créer une fonction pour trouver le début et la fin de la zone d'aterissage par rapport au tableau plateau
    zone_atterissage_debut = 2000
    zone_atterissage_fin = 3500
    zone_parfaite = 2750
    if 3500 > variables_fin['X'] > 2000:
        var_parfaite = np.where(coordonnee == zone_parfaite)
        distance_zone_aterissage = abs(var[0][0] - var_parfaite[0][0])
    else:
        var_debut = np.where(coordonnee == zone_parfaite)
        distance_zone_aterrisage_debut = abs(var[0][0] - var_debut[0][0])
        var_fin = np.where(coordonnee == zone_parfaite)
        distance_zone_aterrisage_fin = abs(var[0][0] - var_fin[0][0])
        distance_zone_aterissage = min([distance_zone_aterrisage_debut, distance_zone_aterrisage_fin])

    distance_totale = distance_altitude_point + distance_zone_aterissage
    variables_fin['hSpeed'] = -50
    variables_fin['fuel'] = 1000
    variables_fin['rotate'] = 90
    return distance_totale


def evaluationV2(simulationEnCours: MarsLanderSim):
    # variables_fin = dict_global[len(dict_global) - 2]
    plateau = simulationEnCours.plateau

    coordonnee = plateau[0]
    coordonnee = np.array(coordonnee)
    var = np.where(coordonnee == int(simulationEnCours.x))
    if simulationEnCours.y < plateau[1][var[0][0]]:
        distance_altitude_point = 0
    else:
        distance_altitude_point = abs(plateau[1][var[0][0]] - simulationEnCours.y)
    # créer une fonction pour trouver le début et la fin de la zone d'aterissage par rapport au tableau plateau
    zone_atterissage_debut, zone_atterissage_fin = att.zoneAtterissage(simulationEnCours.plateau)
    zone_parfaite = zone_atterissage_debut + zone_atterissage_fin / 2
    if zone_atterissage_fin > simulationEnCours.x > zone_atterissage_debut:
        var_parfaite = np.where(coordonnee == zone_parfaite)
        distance_zone_aterissage = abs(var[0][0] - var_parfaite[0][0])
    else:
        var_debut = np.where(coordonnee == zone_parfaite)
        distance_zone_aterrisage_debut = abs(var[0][0] - var_debut[0][0])
        var_fin = np.where(coordonnee == zone_parfaite)
        distance_zone_aterrisage_fin = abs(var[0][0] - var_fin[0][0])
        distance_zone_aterissage = min([distance_zone_aterrisage_debut, distance_zone_aterrisage_fin])

    distance_totale = distance_altitude_point + distance_zone_aterissage
    """    variables_fin['hSpeed'] = -50
    variables_fin['fuel'] = 1000
    variables_fin['rotate'] = 90"""

    return distance_totale


def newSimulation(save_try, randomm, taux_tour, periode, best_score):
    if randomm:
        new_rotate = random.randint(-90, 90)
        new_power = random.randint(0, 4)
    else:
        if periode in save_try[best_score]:
            alea = random.randint(0, 9)
            if taux_tour * 10 > alea:
                new_rotate = save_try[best_score][periode]['rotate']
                new_power = save_try[best_score][periode]['power']
            else:
                new_rotate = random.randint(-90, 90)
                new_power = random.randint(0, 4)
        else:
            new_rotate = random.randint(-90, 90)
            new_power = random.randint(0, 4)

    return new_rotate, new_power


def newSimulationV2(save_try, periode, simulation_en_cours: MarsLanderSim):
    if simulation_en_cours.random:
        new_rotate = random.randint(-90, 90)
        new_power = random.randint(0, 4)
    else:
        if periode in save_try[simulation_en_cours.best_score]:
            alea = random.randint(0, 9)
            if simulation_en_cours.taux_tour * 10 > alea:
                new_rotate = save_try[simulation_en_cours.best_score][periode]['rotate']
                new_power = save_try[simulation_en_cours.best_score][periode]['power']
            else:
                new_rotate = random.randint(-90, 90)
                new_power = random.randint(0, 4)
        else:
            new_rotate = random.randint(-90, 90)
            new_power = random.randint(0, 4)

    return new_rotate, new_power
