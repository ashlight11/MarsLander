import time

from matplotlib import pyplot as plt

import atterissage as att
from affichage import construction_plateau_bis


class MarsLanderSim:
    def __init__(self, plateau, init_data, nb_essais=1000, nb_atterissages=20, taux=0.5):

        self.plateau = construction_plateau_bis(plateau)
        self.best_try = {}
        self.best_score = 10000
        self.periode = 0
        self.dico_atterissage = None
        self.power = None
        self.rotate = None
        self.fuel = None
        self.vs = None
        self.hs = None
        self.y = None
        self.x = None
        self.tracex = []
        self.tracey = []
        self.nb_atterissages = nb_atterissages
        self.nb_essais = nb_essais
        self.taux_tour = taux

        self.perform_init(init_data)

        for i in range(self.nb_essais):
            save_try = self.best_try

            if i == 0:
                self.random = True
            else:
                self.random = False
            for j in range(self.nb_atterissages):
                score_obtenu, self, succes = att.lancementV2(simulationEnCours=self, save_try=save_try)
                save_try[score_obtenu] = self.dico_atterissage
                self.perform_init(init_data)
            new_dic = sorted(save_try.items(), key=lambda t: t[0])
            for key, value in new_dic:
                self.best_try[key] = value
                self.best_score = key
                break
            print("best : ", self.best_score)
            print("vspeed = ", save_try[self.best_score][len(save_try[self.best_score]) - 1]['vSpeed'])
            print("hspeed = ", save_try[self.best_score][len(save_try[self.best_score]) - 1]['hSpeed'])
            print("rotate = ", save_try[self.best_score][len(save_try[self.best_score]) - 1]['rotate'])
            print("X = ", save_try[self.best_score][len(save_try[self.best_score]) - 1]['X'])
            print("nb_tours = ", i)
            test = self.tracex
            # affichageV2(plateau,self.tracex,self.tracey)
            if succes:
                plt.pause(20)
                break
            else:
                plt.close('all')

    def perform_init(self, init_data):
        self.periode = 0
        self.x, self.y, self.hs, self.vs, self.fuel, self.rotate, self.power = [int(i) for i in init_data.split()]
        # print(self.x, self.y, self.hs, self.vs, self.fuel, self.rotate, self.power)
        self.dico_atterissage = {}
        self.sim_to_dict(0)

    def sim_to_dict(self, loop):

        dict_variable = {'periode': self.periode, 'X': self.x, 'Y': self.y, 'hSpeed': self.hs, 'vSpeed': self.vs,
                         'fuel': self.fuel, 'rotate': self.rotate, 'power': self.power, 'tracex': self.tracex,
                         'tracey': self.tracey}
        self.dico_atterissage[loop] = dict_variable


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_first = "5000 2500 -50 0 1000 0 0"  # (X Y hSpeed vSpeed fuel rotate power)
    ground = [(0, 1500), (1000, 2000), (2000, 500), (3500, 500), (5000, 1500), (6999, 1000)]
    ground_level2 = [(0, 100), (1000, 500), (1500, 100), (3000, 100), (3500, 500), (3700, 200), (5000, 1500),
                     (5800, 300), (6000, 1000), (6999, 2000)]
    ground_level3 = [(0, 100), (1000, 500), (1500, 1500), (3000, 1000), (4000, 150), (5500, 150), (6999, 800)]
    ground_level4 = [(0, 1000), (300, 1500), (350, 1400), (500, 2000), (800, 1800), (1000, 2500), (1200, 2100),
                     (1500, 2400), (2000, 1000), (2200, 500), (2500, 100), (2900, 800), (3000, 500), (3200, 1000),
                     (3500, 2000), (3800, 800), (4000, 200), (5000, 200), (5500, 1500), (6999, 2800)]
    ground_level5 = [(0, 1000), (300, 1500), (350, 1400), (500, 2100), (1500, 2100), (2000, 200), (2500, 500),
                     (2900, 300), (3000, 200), (3200, 1000), (3500, 500), (3800, 800), (4000, 200), (4200, 800),
                     (4800, 600), (5000, 1200), (5500, 900), (6000, 500), (6500, 300), (6999, 500)]

    ground_level_grotte = [(0, 200), (1500, 500), (3000, 200), (5500, 200), (4500, 1000), (2500, 1500), (3500, 1500),
                            (6999, 1600)]
    start_time = time.time()
    simulation = MarsLanderSim(ground, input_first)
    print("--- %s seconds ---" % (time.time() - start_time))
