import random

def evaluation(dict_global):
    variables_fin = dict_global[len(dict_global)]
    plateau = dict_global['plateau']
    distance_altitude_point = plateau[variables_fin['X']] - variables_fin['Y']
    distance_zone_aterrisage = 0000000
    variables_fin['hSpeed'] = -50
    variables_fin['fuel'] = 1000
    variables_fin['rotate'] = 90
    print()

def newSimulation(save_try):
    new_rotate = random.randint(-90,90)
    new_power = random.randint(0,4)
    return new_rotate,new_power