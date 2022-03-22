from atterissage import lancement
import matplotlib.pyplot as plt
import time


def main():
    save_best_try = {}
    best_score = 10000
    nb_try = 1000
    for i in range(nb_try):
        save_try = save_best_try
        plateau_def = [0, 1000, 2000, 3500, 5000, 6999, 1500, 2000, 500, 500, 1500, 1000]
        # en utilisant le format correct
        # plateau_def = [(0, 1500), (1000, 2000), (2000, 500), (3500, 500), (5000, 1500), (6999, 1000)]
        nb_aterissage = 100
        X = 5000
        Y = 2500
        hSpeed = -50
        vSpeed = 0
        fuel = 1000
        rotate = 90
        power = 0
        if i == 0:
            random = True
        else:
            random = False
        #taux_tour = i / nb_try
        taux_tour = 0.3
        for j in range(nb_aterissage):
            score_obtenu, aterissage = lancement(save_try, plateau_def, X, Y, hSpeed, vSpeed, fuel, rotate, power,
                                                 random, taux_tour, best_score)
            save_try[score_obtenu] = aterissage
        new_dic = sorted(save_try.items(), key=lambda t: t[0])
        save_best_try = {}
        for key, value in new_dic:
            save_best_try[key] = value
            best_score = key
            break
        print("meilleur score = ",best_score)
        test1 = save_try[best_score]
        test2 = len(save_try[best_score])
        print("vspeed = ", save_try[best_score][len(save_try[best_score])-2]['vSpeed'])
        print("hspeed = ", save_try[best_score][len(save_try[best_score]) - 2]['hSpeed'])
        print("rotate = ", save_try[best_score][len(save_try[best_score]) - 2]['rotate'])
        print("nb_tours = ", i)
        plt.close('all')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
