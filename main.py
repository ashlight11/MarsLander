import numpy as np

def main():
    return 0

def next_periode(attributs,periode_actuelle):
    periode_suivante = periode_actuelle + attribution(attributs)
    return periode_suivante

def attribution(anciens_attributs):
    nouveaux_attributs = 0
    #truc aléatoire d'apprentissage
    if contraintes_attribution(anciens_attributs,nouveaux_attributs):
        return nouveaux_attributs
    else: attribution(anciens_attributs)

def contraintes_attribution(anciens,nouveaux):
    if np.abs(np.abs(anciens['rotate']) - np.abs(anciens['rotate'])) >15 or np.abs(np.abs(anciens['power']) - np.abs(anciens['power'])) >1:
        return False
    else: return True


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
    dict_varaible['plateau'] = construction_plateau(0,1000,2000,3500,5000,6999,1500,2000,500,500,1500,1000)




def construction_plateau(landx0,landx1,landxdebut,landxfin,landx2,landx3,landy0,landy1,landydebut,landyfin,landy2,landy3):
    plateau = np.array([[]])
    plateau[landx0][landy0] = '.'
    step = (landy1-landy0)/(landx1-landx0)
    landynext = landy0
    for i in range(0,landx1-landx0):
        landynext = landynext + step
        plateau[landx0+i][int(landynext)] = '.'

    step = (landydebut - landy1) / (landxdebut - landx1)
    for i in range(0,landxdebut - landx1):
        landynext = landynext + step
        plateau[landy1 + i][int(landynext)] = '.'

    step = (landyfin - landydebut) / (landxfin - landxdebut)
    for i in range(0,landxfin - landxdebut):
        landynext = landynext + step
        plateau[landxdebut + i][int(landynext)] = '.'

    step = (landy2 - landyfin) / (landx2 - landxfin)
    for i in range(0,landx2 - landxfin):
        landynext = landynext + step
        plateau[landxfin + i][int(landynext)] = '.'

    step = (landy3 - landy2) / (landx3 - landx2)
    for i in range(0, landx3 - landx2):
        landynext = landynext + step
        plateau[landx2 + i][int(landynext)] = '.'

    return plateau



def check_contraintes(attributs):
    if(attributs['X'] < 0 or attributs['X'] > 7000
       or attributs['Y'] < 0 or attributs['Y'] > 3000
       or attributs['surfaceN'] < 2 or attributs['surfaceN'] > 30
       or attributs['hSpeed'] < -500 or attributs['hSpeed'] > 500
       or attributs['vSpeed'] < -500 or attributs['vSpeed'] > 500
       or attributs['fuel'] < 0 or attributs['fuel'] > 2000
       or attributs['rotate'] < -90 or attributs['rotate'] > 90
       or attributs['power'] < 0 or attributs['power'] > 4
    ):# + temps de réponse  pour un tours + vérifier de ne pas arriver trop vite au moment de se poser
        return False
    else: return True



main()