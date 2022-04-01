import math

import numpy as np

import MarsLanderSim
from AlgoGene import newSimulationV2, evaluationV2
from affichage import affichageV2

succes = False

# vérification des contraites et de la réussite ou non de l'aterissage
def check_contraintes(dict_varaible, plateau):
    # print("check : ", dict_varaible)
    if dict_varaible['X'] <= 0 or dict_varaible['X'] > 7000:
        print('erreur X')
        return False
    elif dict_varaible['Y'] <= 0 or dict_varaible['Y'] > 3000:
        print('erreur Y')
        return False
    coordonnee = plateau[0]
    coordonnee = np.array(coordonnee)

    atterissage_debut, atterissage_fin = zoneAtterissagebis(plateau)

    var = np.where(coordonnee == int(dict_varaible['X']))
    if len(var[0]) == 3:
        if (dict_varaible['Y'] < plateau[1][var[0][0]] and dict_varaible['Y'] > plateau[1][var[0][1]]):
            if abs(dict_varaible['vSpeed']) <= 40 and dict_varaible['rotate'] == 0 and abs(
                    dict_varaible['hSpeed']) <= 20 and atterissage_fin > dict_varaible['X'] > atterissage_debut:
                print('Réussite')
                global succes
                succes = True
            else:
                #  print('crash')
                v = 1
            return False
        elif (dict_varaible['Y'] > plateau[1][var[0][1]] and dict_varaible['Y'] < plateau[1][var[0][2]]):
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
        elif dict_varaible['power'] < 0 or dict_varaible['power'] > 4:
            # or dict_varaible['surfaceN'] < 2 or dict_varaible['surfaceN'] > 30
            print('erreur power')
            return False
        else:
            return True
    else:
        if dict_varaible['Y'] < plateau[1][var[0][0]]:
            if abs(dict_varaible['vSpeed']) <= 40 and dict_varaible['rotate'] == 0 and abs(
                    dict_varaible['hSpeed']) <= 20 and atterissage_fin > dict_varaible['X'] > atterissage_debut:
                print('Réussite')
                succes = True
            else:
                #  print('crash')
                v = 1
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
        elif dict_varaible['power'] < 0 or dict_varaible['power'] > 4:
            # or dict_varaible['surfaceN'] < 2 or dict_varaible['surfaceN'] > 30
            print('erreur power')
            return False
        else:
            return True
        # rajouter vérif de si on se pose de l'angle et la vitesse

# comme pour la partie codding game
def simulationV2(simulationEnCours: MarsLanderSim, power, rotate):
    x = simulationEnCours.x
    y = simulationEnCours.y
    hs = simulationEnCours.hs
    vs = simulationEnCours.vs
    f = simulationEnCours.fuel
    g = -3.711

    if abs(simulationEnCours.power - power) == 1 or simulationEnCours.power == power:
        simulationEnCours.power = power
    elif simulationEnCours.power < power:
        simulationEnCours.power = simulationEnCours.power + 1
    else:
        simulationEnCours.power = simulationEnCours.power - 1

    if abs(rotate) < 15 or simulationEnCours.rotate == rotate:
        simulationEnCours.rotate = rotate
    else:
        simulationEnCours.rotate = simulationEnCours.rotate + math.copysign(15, rotate)
    simulationEnCours.rotate = math.copysign(90, simulationEnCours.rotate) if (
            abs(simulationEnCours.rotate) > 90) else simulationEnCours.rotate

    new_vs = vs + g + simulationEnCours.power * math.cos(simulationEnCours.rotate * math.pi / 180)

    new_hs = hs - simulationEnCours.power * math.sin(simulationEnCours.rotate * math.pi / 180)

    new_x = x + (new_hs + hs) / 2
    new_y = y + (new_vs + vs) / 2
    new_fuel = f - simulationEnCours.power

    simulationEnCours.x = new_x
    simulationEnCours.y = new_y
    simulationEnCours.hs = new_hs
    simulationEnCours.vs = new_vs
    simulationEnCours.fuel = new_fuel
    simulationEnCours.periode += 1

    simulationEnCours.tracex.append(simulationEnCours.x)
    simulationEnCours.tracey.append(simulationEnCours.y)
    return simulationEnCours

# comme pour la partie codding game
def lancementV2(simulationEnCours: MarsLanderSim, save_try):
    tracex = []
    tracey = []
    loop = 0
    sim = simulationEnCours
    while check_contraintes(sim.dico_atterissage[loop], sim.plateau):
        new_rotate, new_power = newSimulationV2(save_try, loop, sim)
        sim = simulationV2(sim, new_power, new_rotate)
        sim.sim_to_dict(loop + 1)
        # print(sim.x, sim.y, sim.hs, sim.vs, sim.fuel, sim.rotate, sim.power)
        # print(sim.dico_atterissage[loop])
        tracey.append(sim.y)
        tracex.append(sim.x)
        if succes is True:
            break
        # affichageV2(sim.plateau, tracex, tracey)
        loop += 1
    if save_try:
        for key in save_try:
            best_score = key
        affichageV2(sim.plateau, tracex, tracey, succes, best_score)
    else:
        affichageV2(sim.plateau, tracex, tracey, succes, 'xxxx')
    return evaluationV2(sim), sim, succes


# comme pour la partie codding game
def zoneAtterissagebis(plateau):
    begin_flat = 0
    end_flat = 0
    for i in range(len(plateau[1]) - 1):
        if plateau[1][i] == plateau[1][i + 1]:
            begin_flat = plateau[0][i]
            while plateau[1][i] == plateau[1][i + 1]:
                i += 1
            end_flat = plateau[0][i]
            return begin_flat, end_flat

    return begin_flat, end_flat
