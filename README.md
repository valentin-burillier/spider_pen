# Description

Ce depot montre comment réaliser un traceur à partir de l'ensemble LEGO Boost 17101. Il comprend :
- Les instructions de montage du modèle : [docs/building_instructions](https://github.com/valentin-burillier/spiderpen/blob/main/docs/building_instructions.pdf)
- La librairie python permettant le contrôle du robot : [spiderpen](https://github.com/valentin-burillier/spiderpen/tree/main/spiderpen)
- Des exemples d'utilisation : [examples](https://github.com/valentin-burillier/spiderpen/tree/main/examples)
- Toute la documentation nécessaire : [docs](https://github.com/valentin-burillier/spiderpen/tree/main/docs)

<p align="center" width="100%">
    <img width="40%" src="https://user-images.githubusercontent.com/93446869/179176539-6ae127de-4147-4afc-b315-70d8e9002690.jpg">
</p>

Pour rendre le pilotage du robot simple et accessible à tout le monde, le codage des déplacements se fait à la manière turtle, voir [docs/docs](https://github.com/valentin-burillier/spiderpen/blob/main/docs/docs.md).

# Démo

Pour tester la première fois le modèle, veuillez utiliser ce [fichier](https://github.com/valentin-burillier/spiderpen/tree/main/test/demo.py). Il permet de réaliser le tracé suivant :

<p align="center" width="100%">
    <img width="50%" src="https://user-images.githubusercontent.com/93446869/179033485-693fdbc0-0fcc-4398-8c2a-5bdf4143ba4c.jpg">
</p>

Cela permet de mettre en évidence / vérifier :
- La bonne communication entre l'ordinateur et le Hub
- La rectitude des lignes tracées
- L'accesibilité à la zone maximale de dessin

- Le respect des longueurs de chacun des rubans : `L_G` et `L_D`
- Le respect des longueurs tracées : Dx correspond à une demie longueur à l'horizontal et Dy une demie longueur à la verticale

Chacun de ces critères ne sont pas vérifier parfaitemt par le modèle. Ils dépendent principalement des mesures initiales des longueurs des rubans `L_Gi` et `LD_i` (Voir [docs/docs](https://github.com/valentin-burillier/spiderpen/blob/main/docs/docs.md) pour plus d'info).
En générale, les lignes ne sont pas parfaitement rectilignes. Il y a une déviation. Et les longueurs sont conforme à 2-3% près.

Si l'étalonnage correspond à vos attentes en terme de qualité de tracé, vous pouvez utiliser les valeurs afficher pour `L_G` et `L_D` comme longueurs initiales pour la prochaine connection.

# Examples

<p align="center" width="100%">
    <img width="49%" src="https://user-images.githubusercontent.com/93446869/179190675-196e5ab6-85cf-4cc2-a4e9-f096deb4ad0e.jpg">
    <img width="49%" src="https://user-images.githubusercontent.com/93446869/179190701-a03bc5a8-1ae3-4d99-bd7b-6dd275e11dee.jpg">    
</p>

# Installation

_Veuillez noter que la bibliothèque `pylgbst` necessite l'installation de bibliothèques pour le controle Bluetooth comme indiqué [ici](https://github.com/undera/pylgbst/blob/master/README.md)._

Installez la bibliothèque "spiderpen" comme ça :
```bash
pip install spiderpen
```

# Disclamer

- Ce modèle reste compliqué à mettre en place d'un point de vue hardware : Il peut se décrocher, se démonter et les rubans peuvent s'emmêler. Soyez patient !
- La bibliothèque n'est pas parfaite, des bugs peuvent avoir lieu. Dans ce cas, merci de les signaler pour pouvoir les résoudre.
- Des fautes d'orthographes ou des imprécisions peuvent également se cacher dans ce dépot. 
- Partagez les applications cool que vous avez fait ( :

# TODO

- creer le fichier test/demo
- compléter docs/hardware.md
- corriger les fautes d'orthographes
- mettre les exemples d'utilisation
- rédiger le fichier documentant le fonctionnement de l'algorithme de déplacement
- angliser le tout

# Links

- https://www.youtube.com/watch?v=HU9SaCFnCng / https://www.youtube.com/watch?v=5x0n29MjIi8 - les videos qui ont inspiré ce répertoire
- https://github.com/undera/pylgbst - la librairie permettant le controle du Hub
