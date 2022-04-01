import matplotlib.pyplot as plt

# comme pour la partie codding game
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
    plt.show()

    return plateau

# affichage en plot des trajectoire de chacun des essais
def affichageV2(plateau, tracex, tracey, succes, best_score):
    plt.xlim(0, 7000)
    plt.ylim(0, 3000)
    plt.plot(plateau[0], plateau[1], color="blue")
    # plt.plot(X, Y, marker="o", color="red")
    # print(tracex, tracey)
    if succes:
        plt.plot(tracex, tracey, color="green", linewidth=2)
    else:
        # plt.title(str(best_score))
        plt.plot(tracex, tracey, color="red", linewidth=0.5)
    # plt.ion()
    # plt.draw()
    plt.pause(0.001)
