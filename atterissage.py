import math
import numpy as np

import MarsLanderSim
from AlgoGene import newSimulation, evaluation, newSimulationV2, evaluationV2
from affichage import construction_plateau, affichage, affichageV2, construction_plateau_bis


def init(plateau_def, X, Y, hSpeed, vSpeed, fuel, rotate, power):
    dict_global = {}
    dict_varaible = {}
    dict_varaible['periode'] = 0
    dict_varaible['X'] = X
    dict_varaible['Y'] = Y
    dict_varaible['hSpeed'] = hSpeed
    dict_varaible['vSpeed'] = vSpeed
    dict_varaible['fuel'] = fuel
    dict_varaible['rotate'] = rotate
    dict_varaible['power'] = power
    dict_global['plateau'] = construction_plateau(plateau_def)
    # TODO : regarder cet ajout
    # la fonction "bis" permet de construire le plateau avec le format de données en entrée de codingame
    # dict_global['plateau'] = construction_plateau_bis(plateau_def)
    dict_global[0] = dict_varaible
    return dict_global


def check_contraintes(dict_varaible, plateau):
    crash = False
    loop = 0
    if dict_varaible['X'] <= 0 or dict_varaible['X'] > 7000:
        print('erreur X')
        return False
    elif dict_varaible['Y'] <= 0 or dict_varaible['Y'] > 3000:
        print('erreur Y')
        return False
    coordonnee = plateau[0]
    coordonnee = np.array(coordonnee)
    var = np.where(coordonnee == int(dict_varaible['X']))
    if dict_varaible['Y'] < plateau[1][var[0][0]]:
        print('crash')
        return False
    elif dict_varaible['hSpeed'] < -500 or dict_varaible['hSpeed'] > 500:
        print('erreur hSpeed')
        return False
    elif dict_varaible['vSpeed'] < -500 or dict_varaible['vSpeed'] > 500:
        print('erreur vSpeed')
        return False
    elif dict_varaible['fuel'] < 0 or dict_varaible['fuel'] > 2000:
        print('erreur fuel')
        return False
    elif dict_varaible['rotate'] < -90 or dict_varaible['rotate'] > 90:
        print('erreur rotate')
        return False
    elif dict_varaible['power'] < 0 or dict_varaible[
        'power'] > 4:  # or dict_varaible['surfaceN'] < 2 or dict_varaible['surfaceN'] > 30
        print('erreur power')
        return False
    else:
        return True
        # rajouter vérif de si on se pose de l'angle et la vitesse


def check_contraintesV2(simulationEnCours: MarsLanderSim):
    crash = False
    loop = 0
    if simulationEnCours.x <= 0 or simulationEnCours.x > 7000:
        print('erreur X')
        return False
    elif simulationEnCours.y <= 0 or simulationEnCours.y > 3000:
        print('erreur Y')
        return False
    coordonnee = simulationEnCours.plateau[0]
    coordonnee = np.array(coordonnee)
    var = np.where(coordonnee == int(simulationEnCours.x))
    if simulationEnCours.y < simulationEnCours.plateau[1][var[0][0]]:
        return False
    elif simulationEnCours.hs < -500 or simulationEnCours.hs > 500:
        print('erreur hSpeed')
        return False
    elif simulationEnCours.vs < -500 or simulationEnCours.vs > 500:
        print('erreur vSpeed')
        return False
    elif simulationEnCours.fuel < 0 or simulationEnCours.fuel > 2000:
        print('erreur fuel')
        return False
    elif simulationEnCours.rotate < -90 or simulationEnCours.rotate > 90:
        print('erreur rotate')
        return False
    elif simulationEnCours.power < 0 or simulationEnCours.power > 4:  # or dict_varaible['surfaceN'] < 2 or dict_varaible['surfaceN'] > 30
        print('erreur power', simulationEnCours.power)
        return False
    else:
        return True
        # rajouter vérif de si on se pose de l'angle et la vitesse


def simulation(dict_varaible, new_power, new_rotate):
    g = -3.711
    if abs(dict_varaible['power'] - new_power) == 1 or dict_varaible['power'] == new_power:
        dict_varaible['power'] = new_power
    elif dict_varaible['power'] < new_power:
        dict_varaible['power'] = dict_varaible['power'] + 1
    else:
        dict_varaible['power'] = dict_varaible['power'] - 1

    if abs(dict_varaible['rotate'] - new_rotate) < 15 or dict_varaible['rotate'] == new_rotate:
        dict_varaible['rotate'] = new_rotate
    elif dict_varaible['rotate'] < new_rotate:
        dict_varaible['rotate'] + math.copysign(15, new_rotate)
    else:
        dict_varaible['rotate'] - math.copysign(15, new_rotate)

    dict_varaible['vSpeed'] = dict_varaible['vSpeed'] + (g + dict_varaible['power']) * math.sin(
        dict_varaible['rotate'] * math.pi / 180)
    dict_varaible['hSpeed'] = dict_varaible['hSpeed'] + dict_varaible['vSpeed'] * math.cos(
        dict_varaible['rotate'] * math.pi / 180)
    dict_varaible['X'] = dict_varaible['X'] + dict_varaible['hSpeed']
    dict_varaible['Y'] = dict_varaible['Y'] + dict_varaible['vSpeed']
    dict_varaible['fuel'] = dict_varaible['fuel'] - dict_varaible['power']
    dict_varaible['periode'] = dict_varaible['periode'] + 1
    return dict_varaible


def simulationV2(simulationEnCours: MarsLanderSim, new_power, new_rotate):
    g = -3.711
    if abs(simulationEnCours.power - new_power) == 1 or simulationEnCours.power == new_power:
        simulationEnCours.power = new_power
    elif simulationEnCours.power < new_power:
        simulationEnCours.power = simulationEnCours.power + 1
    else:
        simulationEnCours.power = simulationEnCours.power - 1

    if abs(simulationEnCours.rotate - new_rotate) < 15 or simulationEnCours.rotate == new_rotate:
        simulationEnCours.rotate = new_rotate
    elif simulationEnCours.rotate < new_rotate:
        simulationEnCours.rotate + math.copysign(15, new_rotate)
    else:
        simulationEnCours.rotate - math.copysign(15, new_rotate)

    simulationEnCours.vs = simulationEnCours.vs + (g + simulationEnCours.power) * math.sin(
        simulationEnCours.rotate * math.pi / 180)
    simulationEnCours.hs = simulationEnCours.hs + simulationEnCours.vs * math.cos(
        simulationEnCours.rotate * math.pi / 180)
    simulationEnCours.x = simulationEnCours.x + simulationEnCours.hs
    simulationEnCours.y = simulationEnCours.y + simulationEnCours.vs
    simulationEnCours.fuel = simulationEnCours.fuel - simulationEnCours.power
    simulationEnCours.periode = simulationEnCours.periode + 1

    return simulationEnCours


def lancement(save_try, plateau_def, X, Y, hSpeed, vSpeed, fuel, rotate, power, random, nb_tours, best_score):
    dico_atterissage = init(plateau_def, X, Y, hSpeed, vSpeed, fuel, rotate, power)
    tracex = []
    tracey = []
    loop = 0

    while check_contraintes(dico_atterissage[loop], dico_atterissage['plateau']):
        new_rotate, new_power = newSimulation(save_try, random, nb_tours, loop, best_score)
        dico_atterissage[loop + 1] = simulation(dico_atterissage[loop], new_power, new_rotate).copy()
        tracey.append(dico_atterissage[loop]['Y'])
        tracex.append(dico_atterissage[loop]['X'])
        affichage(dico_atterissage, tracex, tracey)
        loop += 1
    return evaluation(dico_atterissage), dico_atterissage


def zoneAtterissage(plateau):
    begin_flat = 0
    end_flat = 0
    for index, element in enumerate(plateau):
        if index != len(plateau) - 1 and element[1] == plateau[index + 1][1]:
            begin_flat = element
            end_flat = plateau[index + 1]

    return begin_flat, end_flat


def lancementV2(simulationEnCours: MarsLanderSim, save_try):
    tracex = []
    tracey = []
    loop = 0
    while check_contraintesV2(simulationEnCours):
        new_rotate, new_power = newSimulationV2(save_try, loop, simulationEnCours)
        simulationEnCours.dico_atterissage[loop + 1] = simulationV2(simulationEnCours, new_power,
                                                                    new_rotate).sim_to_dict().copy()
        tracey.append(simulationEnCours.y)
        tracex.append(simulationEnCours.x)
        affichageV2(simulationEnCours.plateau, tracex, tracey)
        loop += 1
    return evaluationV2(simulationEnCours)
