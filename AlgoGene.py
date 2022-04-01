import random

import numpy as np

import atterissage as att
from MarsLanderSim import MarsLanderSim

# fonction d'évaluation
def evaluationV2(simulationEnCours: MarsLanderSim):

    plateau = simulationEnCours.plateau
    if simulationEnCours.x <= 0 or simulationEnCours.x >= 6999 or simulationEnCours.y <= 0 or simulationEnCours.y >= 2999:
        return 100000

    # évaluation de l'altitude
    var = plateau[0].index(int(simulationEnCours.x))
    if simulationEnCours.y < plateau[1][var]:
        distance_altitude_point = 0
    else:
        distance_altitude_point = abs(plateau[1][var] - simulationEnCours.y)

    # évaluation de l'altitude
    zone_atterissage_debut, zone_atterissage_fin = att.zoneAtterissagebis(simulationEnCours.plateau)
    zone_parfaite = zone_atterissage_debut + zone_atterissage_fin / 2
    if zone_atterissage_fin > simulationEnCours.x > zone_atterissage_debut:
        distance_zone_aterissage = 0
    else:
        var_debut = plateau[0].index(int(zone_parfaite))
        distance_zone_aterrisage_debut = abs(var - var_debut)
        var_fin = var_debut
        distance_zone_aterrisage_fin = abs(var - var_fin)
        distance_zone_aterissage = (min([distance_zone_aterrisage_debut, distance_zone_aterrisage_fin])) * 10

    # évaluation de la vitesse verticale
    if abs(simulationEnCours.vs) > 40:
        distance_vspeed = (abs(simulationEnCours.vs) - 40) * 2
    else:
        distance_vspeed = 0
    # évaluation de la vitesse horizontale
    if abs(simulationEnCours.hs) > 20:
        distance_hspeed = (abs(simulationEnCours.hs) - 20) * 2
    else:
        distance_hspeed = 0
    # évaluation de l'angle de la fusée
    if simulationEnCours.rotate != 0:
        distance_rotate = (abs(simulationEnCours.rotate)) * 2
    else:
        distance_rotate = 0
    distance_fin = distance_rotate + distance_hspeed + distance_vspeed
    distance_totale = distance_altitude_point + distance_zone_aterissage + distance_fin
    return distance_totale

# comme pour la partie codding game
def newSimulationV2(save_try, periode, simulation_en_cours: MarsLanderSim):
    if simulation_en_cours.random:
        new_rotate = random.randrange(-90, 90, 5)
        new_power = random.randint(3, 4)
    else:
        if periode in save_try[simulation_en_cours.best_score]:
            alea = random.randint(0, 9)
            if simulation_en_cours.taux_tour * 10 > alea:
                new_rotate = save_try[simulation_en_cours.best_score][periode]['rotate']
                new_power = save_try[simulation_en_cours.best_score][periode]['power']
            else:
                new_rotate = random.randrange(-90, 90, 5)
                new_power = random.randint(3, 4)
        else:
            new_rotate = random.randrange(-90, 90, 5)
            new_power = random.randint(3, 4)

    return new_rotate, new_power
