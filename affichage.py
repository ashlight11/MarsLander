import numpy as np
import matplotlib.pyplot as plt

def construction_plateau(plateau_def):
    plateau = []
    taille = len(plateau_def)
    X = plateau_def[0]
    Y = plateau_def[int(taille/2)]
    coordx = []
    coordy = []
    coordx.append(X)
    coordy.append(Y)
    plateau.append(coordx)
    plateau.append(coordy)
    landynext = plateau_def[int(taille/2)]
    landxnext = plateau_def[0]
    loop = 0
    while loop < taille/2-1:
        stepy = (plateau_def[int(taille/2)+1+loop] - plateau_def[int(taille/2)+loop]) / abs((plateau_def[loop+1] - plateau_def[loop]))
        stepx = (plateau_def[loop+1] - plateau_def[loop])/abs(plateau_def[loop+1] - plateau_def[loop])
        for i in range(0, abs(plateau_def[loop+1] - plateau_def[loop])):
            landxnext = landxnext + stepx
            landynext = stepy + landynext
            plateau[0].append(landxnext)
            plateau[1].append(landynext)
        loop+=1
        """
        plt.xlim(0, 7000)
        plt.ylim(0, 3000)
        plt.plot(plateau)
        plt.show()
        """
    return plateau


def affichage(data,tracex,tracey):
    plateau = data['plateau']
    X = data[len(data)-2]['X']
    Y = data[len(data)-2]['Y']
    plt.xlim(0, 7000)
    plt.ylim(0, 3000)
    plt.plot(plateau[0],plateau[1],color="blue")
    #plt.plot(X, Y, marker="o", color="red")
    plt.plot(tracex,tracey,color="red")
    plt.ion()
    plt.draw()
    plt.pause(0.01)


    