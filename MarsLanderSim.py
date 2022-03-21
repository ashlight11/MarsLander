from matplotlib import pyplot as plt
from affichage import construction_plateau_bis
import atterissage as att


class MarsLanderSim:
    def __init__(self, plateau, init_data, nb_essais=10, nb_atterissages=5, taux=0.5):
        self.plateau = construction_plateau_bis(plateau)
        self.nb_essais = nb_essais
        self.nb_atterissages = nb_atterissages
        self.taux_tour = taux
        self.best_try = {}
        self.best_score = 10000
        self.periode = 0
        self.x, self.y, self.hs, self.vs, self.fuel, self.rotate, self.power = [int(i) for i in init_data.split()]
        print(self.x, self.y, self.hs, self.vs, self.fuel, self.rotate, self.power)
        self.dico_atterissage = self.sim_to_dict()
        print(self.dico_atterissage)

        for i in range(self.nb_essais):
            save_try = self.best_try
            if i == 0:
                self.random = True
            else:
                self.random = False
            for j in range(self.nb_atterissages):
                score_obtenu = att.lancementV2(simulationEnCours=self, save_try=save_try)
                save_try[score_obtenu] = self.sim_to_dict()
            new_dic = sorted(save_try.items(), key=lambda t: t[0])
            for key, value in new_dic:
                self.best_try[key] = value
                self.best_score = key
                break
            plt.close('all')

    def sim_to_dict(self):
        dict_global = {}
        dict_variable = {'periode': self.periode, 'X': self.x, 'Y': self.y, 'hSpeed': self.hs, 'vSpeed': self.vs,
                         'fuel': self.fuel, 'rotate': self.rotate, 'power': self.power}
        dict_global[0] = dict_variable
        return dict_global


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_first = "5000 2500 -50 0 1000 90 0"  # (X Y hSpeed vSpeed fuel rotate power)
    ground = [(0, 1500), (1000, 2000), (2000, 500), (3500, 500), (5000, 1500), (6999, 1000)]
    simulation = MarsLanderSim(ground, input_first)
