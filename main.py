import numpy as np

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import scipy
from scipy import integrate


def __main__():
    simulation()


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


def simulation():
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point.
    # By linking all the points together in a sequential fashion, you form the surface of Mars.
    number_points = 6
    ground = [(0, 1500), (1000, 2000), (2000, 500), (3500, 500), (5000, 1500), (6999, 1000)]
    # hs: the horizontal speed (in m/s), can be negative.
    # vs: the vertical speed (in m/s), can be negative.
    # f: the quantity of remaining fuel in liters.
    # r: the rotation angle in degrees (-90 to 90).
    # p: the thrust power (0 to 4).
    input_first = "5000 2500 -50 0 1000 90 0"  # (X Y hSpeed vSpeed fuel rotate power)
    output_values = "-45 4"
    input_second = "4950 2498 -51 -3 999 75 1"
    input_third = "4898 2493 -53 -6 997 60 2"

    begin_flat, end_flat = find_landing_area(ground)

    estimateNewValues(input_first, output_values)


def estimateNewValues(input_values, output_values):
    x, y, hs, vs, f, r, p = [int(i) for i in input_values.split()]
    rotate, power = [int(i) for i in output_values.split()]

    for i in range(2):
        print(x, y, hs, vs, f, r, p)
        print(rotate, power)
        g = -3.711
        new_power = p + power if power <= 1 else p + 1

        new_r = r + rotate if abs(rotate) < 15 else r + math.copysign(15, rotate)

        new_vs = vs + g + new_power * math.cos(new_r * math.pi / 180)

        new_hs = hs - new_power * math.sin(new_r * math.pi / 180)

        new_x = x + (new_hs + hs) / 2
        new_y = y + (new_vs + vs) / 2
        new_fuel = f - new_power

        print("Turn ", i, " ;",  new_x, new_y, new_hs, new_vs, new_fuel, new_r, new_power)
        print("\n")

        x = new_x
        y = new_y
        hs = new_hs
        vs = new_vs
        f = new_fuel
        r = new_r
        p = new_power


def find_landing_area(ground):
    begin_flat = 0
    end_flat = 0
    for index, element in enumerate(ground):
        if index != len(ground) - 1 and element[1] == ground[index + 1][1]:
            begin_flat = element
            end_flat = ground[index + 1]

    return begin_flat, end_flat


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    simulation()


def initialisation():
    dict_varaible = {}
    dict_varaible['periode'] = 0
    dict_varaible['surfaceN'] = 6
    dict_varaible['X'] = 5000
    dict_varaible['Y'] = 2500
    dict_varaible['hSpeed'] = -50
    dict_varaible['fuel'] = 1000
    dict_varaible['rotate'] = 90
    dict_varaible['power'] = 0
    dict_varaible['plateau'] = construction_plateau(0, 1000, 2000, 3500, 5000, 6999, 1500, 2000, 500, 500, 1500, 1000)


def construction_plateau(landx0, landx1, landxdebut, landxfin, landx2, landx3, landy0, landy1, landydebut, landyfin,
                         landy2, landy3):
    plateau = np.array([[]])
    plateau[landx0][landy0] = '.'
    step = (landy1 - landy0) / (landx1 - landx0)
    landynext = landy0
    for i in range(0, landx1 - landx0):
        landynext = landynext + step
        plateau[landx0 + i][int(landynext)] = '.'

    step = (landydebut - landy1) / (landxdebut - landx1)
    for i in range(0, landxdebut - landx1):
        landynext = landynext + step
        plateau[landy1 + i][int(landynext)] = '.'

    step = (landyfin - landydebut) / (landxfin - landxdebut)
    for i in range(0, landxfin - landxdebut):
        landynext = landynext + step
        plateau[landxdebut + i][int(landynext)] = '.'

    step = (landy2 - landyfin) / (landx2 - landxfin)
    for i in range(0, landx2 - landxfin):
        landynext = landynext + step
        plateau[landxfin + i][int(landynext)] = '.'

    step = (landy3 - landy2) / (landx3 - landx2)
    for i in range(0, landx3 - landx2):
        landynext = landynext + step
        plateau[landx2 + i][int(landynext)] = '.'

    return plateau


def check_contraintes(attributs):
    if (attributs['X'] < 0 or attributs['X'] > 7000
            or attributs['Y'] < 0 or attributs['Y'] > 3000
            or attributs['surfaceN'] < 2 or attributs['surfaceN'] > 30
            or attributs['hSpeed'] < -500 or attributs['hSpeed'] > 500
            or attributs['vSpeed'] < -500 or attributs['vSpeed'] > 500
            or attributs['fuel'] < 0 or attributs['fuel'] > 2000
            or attributs['rotate'] < -90 or attributs['rotate'] > 90
            or attributs['power'] < 0 or attributs['power'] > 4
    ):  # + temps de réponse  pour un tours + vérifier de ne pas arriver trop vite au moment de se poser
        return False
    else:
        return True
