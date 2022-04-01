import sys
import math
import time
import random

class MarsSim:
    def __init__(self, init_data, nb_essais=100, nb_atterissages=100, taux=0.5):

        self.best_try = {}
        self.best_score = 10000000
        self.periode = 0
        self.dico_atterissage = None
        self.power = None
        self.rotate = None
        self.fuel = None
        self.vs = None
        self.hs = None
        self.y = None
        self.x = None
        self.nb_atterissages = nb_atterissages
        self.nb_essais = nb_essais
        self.taux_tour = taux
        self.random = True

        self.perform_init(init_data)
        start_time = time.time()
        j = 0
        # vérification de la fenetre de temps
        while time.time() - start_time < 0.1:
            save_try = self.best_try
            j += 1
            # lancement de la simulation, retourne un dictionnaire avec les essais réalisés
            score_obtenu, self, succes = lancementV2(simulationEnCours=self, save_try=save_try)
            save_try[score_obtenu] = self.dico_atterissage
            self.perform_init(init_data)
        new_dic = sorted(save_try.items(), key=lambda t: t[0])
        # on conserve le meilleur essai pour la suite
        var = plateau[0].index(int(new_dic[0][1][1]['X']))
        if new_dic[0][1][1]['Y'] < plateau[1][var]:
            # si on atteri on met automatiquement la fusée à un angle de 0 (possible seulement si elle à un angle compris en -15 et 15)
            print(0, int(new_dic[0][1][1]['power']))
        else:
            # on envoi le résultat du meilleur essai réalisé
            print(int(new_dic[0][1][1]['rotate']), int(new_dic[0][1][1]['power']))
            print('nb tours ' + str(j), file=sys.stderr, flush=True)

    def perform_init(self, init_data):
        self.periode = 0
        self.x, self.y, self.hs, self.vs, self.fuel, self.rotate, self.power = [int(i) for i in init_data.split()]
        self.dico_atterissage = {}
        self.sim_to_dict(0)

    def sim_to_dict(self, loop):
        dict_variable = {'periode': self.periode, 'X': self.x, 'Y': self.y, 'hSpeed': self.hs, 'vSpeed': self.vs,
                         'fuel': self.fuel, 'rotate': self.rotate, 'power': self.power}
        self.dico_atterissage[loop] = dict_variable


# Construction d'un plateau sous forme plateau = [[x0,y0],[x1,y1],...,[xn,yn]]
def construction_plateau_bis(data):
    plateau = []
    taille = len(data)
    X = data[0][0]
    Y = data[0][1]
    coordx = []
    coordy = []
    coordx.append(X)
    coordy.append(Y)
    plateau.append(coordx)
    plateau.append(coordy)
    landynext = Y
    landxnext = X
    loop = 0
    while loop < taille - 1:
        stepy = (data[1 + loop][1] - data[loop][1]) / abs(
            (data[loop + 1][0] - data[loop][0]))
        stepx = (data[loop + 1][0] - data[loop][0]) / abs(data[loop + 1][0] - data[loop][0])
        for i in range(0, abs(data[loop + 1][0] - data[loop][0])):
            landxnext = landxnext + stepx
            landynext = stepy + landynext
            plateau[0].append(landxnext)
            plateau[1].append(landynext)
        loop += 1

    return plateau


def lancementV2(simulationEnCours: MarsSim, save_try):
    loop = 0
    sim = simulationEnCours
    # trouve le meilleur résultat pour un nombre de pas
    nb_pas = 2
    while check_contraintes(sim.dico_atterissage[loop]) and loop < nb_pas:
        new_rotate, new_power = newSimulationV2(save_try, loop, sim)
        sim = simulationV2(sim, new_power, new_rotate)
        sim.sim_to_dict(loop + 1)
        if succes is True:
            break
        loop += 1
    return evaluationV2(sim), sim, succes


def evaluationV2(simulationEnCours: MarsSim):
    global plateau

    var = plateau[0].index(int(simulationEnCours.x))

    # on resgarde si on est toujours dans les limites du jeux
    if simulationEnCours.x <= 0 or simulationEnCours.x >= 6999 or simulationEnCours.y <= 0 or simulationEnCours.y >= 2999:
        return 100000

    # on resgarde à quelle distance on se situe du sol
    if simulationEnCours.y < plateau[1][var]:
        distance_altitude_point = 0
    else:
        distance_altitude_point = abs(plateau[1][var] - simulationEnCours.y)

    # on resgarde notre distance par rapport à la zone d'aterissage
    zone_atterissage_debut, zone_atterissage_fin = zoneAtterissagebis()
    zone_parfaite = zone_atterissage_debut + zone_atterissage_fin / 2
    if (zone_atterissage_fin - 10) > simulationEnCours.x > (zone_atterissage_debut + 10):
        distance_zone_aterissage = 0
    else:
        var_debut = plateau[0].index(int(zone_parfaite))
        distance_zone_aterrisage_debut = abs(var - var_debut)
        var_fin = var_debut
        distance_zone_aterrisage_fin = abs(var - var_fin)
        distance_zone_aterissage = min([distance_zone_aterrisage_debut, distance_zone_aterrisage_fin]) * 500

    # on s'il y a un point élevé entre nous et la zone d'aterissage
    if var < zone_atterissage_debut:
        carte_hauteurs_fuse_aterissage = sorted(plateau[1][int(var):int(zone_atterissage_debut)], reverse=True)
    else:
        carte_hauteurs_fuse_aterissage = sorted(plateau[1][int(zone_atterissage_fin):int(var)], reverse=True)
    if simulationEnCours.x - 50 > zone_atterissage_fin or simulationEnCours.x + 50 < zone_atterissage_debut:
        if simulationEnCours.y - 600 < carte_hauteurs_fuse_aterissage[0]:
            test = 0
        else:
            test = 1
    else:
        test = 1

    # en fonction de la situation (point élevé entre nous et l'aterissage / au dessus de la zone d'aterissage) on définit les poids pour l'évaluation
    if test == 0:
        if distance_zone_aterissage == 0:
            if abs(simulationEnCours.vs) >= 30:
                distance_vspeed = (abs(simulationEnCours.vs) - 30) * 3000
            else:
                distance_vspeed = 0
            if abs(simulationEnCours.hs) >= 19:
                distance_hspeed = (abs(simulationEnCours.hs) - 19) * 1000

            else:
                distance_hspeed = 0
            if simulationEnCours.rotate != 0:
                distance_rotate = (abs(simulationEnCours.rotate)) * 1000
            else:
                distance_rotate = 0
            distance_fin = distance_rotate + distance_hspeed + distance_vspeed
        else:
            if abs(simulationEnCours.vs) >= 1:
                distance_vspeed = (abs(simulationEnCours.vs) - 1) * 3000
            else:
                distance_vspeed = 0
            if abs(simulationEnCours.hs) >= 25:
                distance_hspeed = (abs(simulationEnCours.hs) - 25) * 1000
            else:
                distance_hspeed = 0
            if simulationEnCours.rotate != 0:
                distance_rotate = (abs(simulationEnCours.rotate)) * 50
            else:
                distance_rotate = 0
            distance_fin = distance_rotate + distance_hspeed + distance_vspeed
    else:
        if abs(simulationEnCours.vs) >= 30:
            distance_vspeed = (abs(simulationEnCours.vs) - 30) * 3000
        else:
            distance_vspeed = 0
        if abs(simulationEnCours.hs) >= 18:
            distance_hspeed = (abs(simulationEnCours.hs) - 18) * 1500
        else:
            distance_hspeed = 0
        if simulationEnCours.rotate != 0:
            distance_rotate = (abs(simulationEnCours.rotate)) * 50
        else:
            distance_rotate = 0
        distance_fin = distance_rotate + distance_hspeed + distance_vspeed
    distance_totale = distance_altitude_point + distance_zone_aterissage + distance_fin
    return distance_totale

# vérification des contraintes imposées
def check_contraintes(dict_varaible):
    if dict_varaible['X'] <= 0 or dict_varaible['X'] > 7000:
        print('erreur X', file=sys.stderr, flush=True)
        return False
    elif dict_varaible['Y'] <= 0 or dict_varaible['Y'] > 3000:
        print('erreur Y', file=sys.stderr, flush=True)
        return False
    var = plateau[0].index(int(dict_varaible['X']))
    if dict_varaible['Y'] < plateau[1][var]:
        return False
    elif dict_varaible['rotate'] < -90 or dict_varaible['rotate'] > 90:
        print('erreur rotate', file=sys.stderr, flush=True)
        return False
    elif dict_varaible['power'] < 0 or dict_varaible['power'] > 4:
        # or dict_varaible['surfaceN'] < 2 or dict_varaible['surfaceN'] > 30
        print('erreur power', file=sys.stderr, flush=True)
        return False
    else:
        return True

# simulation qui retourne selon le power et le rotate, donne la nouvelle position et vitesse de la fusée
def simulationV2(simulationEnCours: MarsSim, power, rotate):
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

    return simulationEnCours

# définition de la vitesse et du power à envoyer
def newSimulationV2(save_try, periode, simulation_en_cours: MarsSim):
    # Aléatoire si nouvelle simulation
    if simulation_en_cours.random:
        new_rotate = random.randrange(-90, 90, 5)
        new_power = random.randint(0, 4)
    else:
        # bassé sur le meilleurs score obtenue lors des essais précédents
        print('pas random total', file=sys.stderr, flush=True)
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

# trouve la zone d'aterissage de la fusée
def zoneAtterissagebis():
    global plateau
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

n = int(input())
surfaces = []
for i in range(n):
    land_x, land_y = [int(j) for j in input().split()]
    surfaces.append([land_x, land_y])

plateau = construction_plateau_bis(surfaces)
start_time = time.time()
succes = False

# game loop
while True:
    simulation = MarsSim(input())
    start_time = time.time()
