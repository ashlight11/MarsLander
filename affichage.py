import numpy as np
import matplotlib.pyplot as plt

def construction_plateau(plateau_def):
    plateau = []
    taille = len(plateau_def)
    plateau.append(plateau_def[int(taille/2)])
    landynext = plateau_def[int(taille/2)]
    loop = 0
    while loop < taille/2-1:
        step = (plateau_def[int(taille/2)+1+loop] - plateau_def[int(taille/2)+loop]) / (plateau_def[loop+1] - plateau_def[loop])
        for i in range(0, plateau_def[loop+1] - plateau_def[loop]):
            landynext = step + landynext
            plateau.append(landynext)
        loop+=1
        """
        plt.xlim(0, 7000)
        plt.ylim(0, 3000)
        plt.plot(plateau)
        plt.show()
        """
    return plateau


def affichage(data,X,Y,trace):
    plateau = data['plateau']
    plt.xlim(0, 7000)
    plt.ylim(0, 3000)
    plt.plot(plateau,color="blue")
    plt.plot(X, Y, marker="o", color="red")
    plt.plot(trace,color="red")
    plt.show()


    