### Ce code est réalisé dans le cadre de l'UV MAD (*Models and Algorithms for Decision*) par Marianne De Poorter et Jules Descotes

## Basé sur le jeu *[Codingame Project](https://www.codingame.com/ide/puzzle/mars-lander)*


L'objectif de ce programme est de faire atterrir, sans crash, la capsule "Mars Lander" qui contient le rover Opportunity. La capsule “Mars Lander” permettant de débarquer le rover est pilotée par un programme qui échoue trop souvent dans le simulateur de la NASA.

Nous utiliserons un algorithm genetic pour résoudre ce problème.


## Utilisation

Deux utilisations sont possibles :

- Une utilisation directement sur le site de *[codding game](https://www.codingame.com/ide/puzzle/mars-lander)* en copiant tout le fichier 'main_for_codding_game.py'
- Une utilisation en local avec un run sur 'MarsLanderSim.py'

Les deux utilisations sont assez similaires si ce n'est que sur le site de codding game, une instruction
doit être donnée toutes les 0,1 seconde.
Considérant cela, pour les tests en local un essai est constitué de l'ensemble des pas entre le lancement de la simulation et le crash ou l'atterrissage de la fusée.
Alors que dans la partie codding game un essai est constitué d'un nombre limité de pas afin de pouvoir respecter le timming.

Avec la restriction de temps à 0,1 seconde, une avance de 2 pas permet de réaliser une centaine d'essais et une avance de 10 pas permet de réaliser une cinquantaine d'essais.


## L'algorithme génétique

Afin de réussir l'atterrissage, un algorithme génétique est utilisé. Cet algorithme reprend les notions vues en cours et chacune des parties composant l'algorithme sont détaillées ci-dessous.

### Initialisation
L'initialisation est totalement aléatoire avec des valeurs pour le power allant de 0 à 4 et des valeurs pour la rotation allant de -90 à 90


### Evaluation
L'évaluation est assez complexe, car va déterminer en grande partie la réussite ou non de l'objectif. 
L'évaluation est évolutive selon les cas de figure suivants :
- La fusée est au-dessus de la zone d'atterrissage. L'évaluation se concentre alors sur la gestion des vitesses latérales, horizontales et de rotation
- La fusée n'est pas au-dessus de la zone et un obstacle est présent entre la fusée et la zone d'atterrissage. L'évaluation se concentre sur un rapprochement de la zone d'atterrissage tout en limitant un maximum la vitesse de chute (vitesse verticale)
- La fusée n'est pas au-dessus de la zone. l'évaluation se concentre sur le rapprochement de la zone d'atterrissage tout évitant de monter trop haut en vitesse de chute.

La gestion de la distance entre la position **Xf** de la fusée et la position **Xa** de la zone d'aterissage ne se fait pas via une distance euclidienne, mais via une distance entre des indexs de liste.     
En effet, la construction du plateau est sous la forme d'une liste avec plateau = [[x0,y0],[x1,y1],...,[xn,yn]]      
Pour trouver la distance, il suffit de faire la différence entre l'index **Xf** et l'index de **Xa**. Cette gestion via index permet la gestion de plateaux plus complexe avec des grottes par exemple.

L'évaluation n'est pas composée uniquement de la distance mais des critères suivant avec des poids variants selon les cas de figures présentés précédement.     
Ci-dessous une présentation des critères utilisés avec les poids présents dans le cas de figure 3.
- Distance entre le sol et la fusée, 1 * distance (1 représentant le poids)
- Angle actuel de la fusée, 50 * angle_actuel
- Distance entre la fusée et la zone d'atterrissage , 200 * (Xf - Xa)
- Vitesse horizontale de la fusée, 1000 * (vitesse horizontale - 18)
- Vitesse verticale de la fusée, 3000 * (vitesse verticale - 35)

La vitesse verticale est limitée à 20 par le jeu mais une marge de sécurité est définie à 18. De même pour la vitesse verticale avec une marge de sécurité à 35.     
La vitesse verticale possède un poids tres important car si la fusée prend trop de vitesse il sera impossible d'éviter le crash


### critère d'arrêt
Correspond à un atterrissage ou à un crash.

### Sélection
La selection permettant de définir les parents est assez simple dans notre cas, elle consiste simplement à garder le meilleur score réalisé lors des essais précédents.     
Cependant, cette sélection n'est pas parfaite et il pourrait être intéressant de conserver le meilleur score parent ainsi que le meilleur score enfant.

### Croisement et mutation
Par manque de temps seul des mutations sont réalisées dans cet algorithme. 
Les mutations sont effectuées sur le meilleur essai réalisé jusqu'à présent via un pourcentage de chance de choisir entre l'action réalisée par le meilleur essai ou une action aléatoire.

Ce fonctionnement permet de trouver une solution d'atterrissage dans la majorité des cas mais avec des croissements entre le meilleur parent et le meilleur enfant une solution pourrait être trouvée plus rapidement.

## Conclusion

Avec notre algorithme actuel nous arrivons à réaliser les situations 1,2,3 et 5 de codding game. Il arrive que la fusée ce crash mais en réessayant quelques fois le code réussi.

De nombreuses améliorations sont encore à réaliser pour avoir un système fiable autant les croissements et mutation que dans la fonction de selection.      
La fonction d'évaluation semble assez complète et remplie assez bien son rôle.

Ce projet à été tres apprécié par notre binôme et nous sommes satisfaits des résultats obtenus en moins de deux semaines.

