from atterissage import lancement

def main():
    save_try = {}
    plateau_def = [0, 1000, 2000, 3500, 5000, 6999, 1500, 2000, 500, 500, 1500, 1000]
    nb_aterissage = 100
    X = 5000
    Y = 2500
    hSpeed = -50
    vSpeed = 0
    fuel = 1000
    rotate = 90
    power = 0
    for i in range(nb_aterissage):
        score_obtenu,aterissage = lancement(save_try,plateau_def,X,Y,hSpeed,vSpeed,fuel,rotate,power)
        save_try[score_obtenu] = aterissage

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()