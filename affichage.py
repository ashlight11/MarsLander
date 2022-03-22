import matplotlib.pyplot as plt





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
