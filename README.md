# Description

Ce dépôt montre comment réaliser un traceur à partir de l'ensemble LEGO Boost 17101. Il comprend :
- Les instructions de montage du modèle : [docs/building_instructions](https://github.com/valentin-burillier/spiderpen/blob/main/docs/building_instructions.pdf)
- La librairie python permettant le contrôle du robot : [spiderpen](https://github.com/valentin-burillier/spiderpen/tree/main/spiderpen)
- Des exemples d'utilisation : [examples](https://github.com/valentin-burillier/spiderpen/tree/main/examples)
- Toute la documentation nécessaire : [docs](https://github.com/valentin-burillier/spiderpen/tree/main/docs)

<p align="center" width="100%">
    <img width="50%" src="https://user-images.githubusercontent.com/93446869/179218640-bc38fe10-068a-4bd8-b7af-3a2945f7dc68.jpg">
</p>

Pour rendre le pilotage du robot simple et accessible à tout le monde, le codage des déplacements se fait à la manière turtle, voir [docs/docs](https://github.com/valentin-burillier/spiderpen/blob/main/docs/docs.md).

# Démo

Pour tester la première fois le modèle, veuillez utiliser ce [fichier](https://github.com/valentin-burillier/spiderpen/tree/main/test/demo.py). Il permet de réaliser le tracé suivant :

<p align="center" width="100%">
    <img width="50%" src="https://user-images.githubusercontent.com/93446869/179033485-693fdbc0-0fcc-4398-8c2a-5bdf4143ba4c.jpg">
</p>

Cela permet de mettre en évidence / vérifier :
- La bonne communication entre l'ordinateur et le Hub.
- La rectitude des lignes tracées.
- L'accesibilité à la zone maximale de dessin.

- Le respect des longueurs de chacun des rubans : `L_G` et `L_D`.
- Le respect des longueurs tracées : Dx correspond à une demi-longueur à l'horizontale et Dy une demi-longueur à la verticale.

Chacun de ces critères n'est pas vérifié parfaitemt par le modèle. Ils dépendent principalement des mesures initiales des longueurs des rubans `L_Gi` et `LD_i` (Voir [docs/docs](https://github.com/valentin-burillier/spiderpen/blob/main/docs/docs.md) pour plus d'info).
En général, les lignes ne sont pas parfaitement rectilignes. Il y a une déviation. Et les longueurs sont conformes à 2-3% près.

Si l'étalonnage correspond à vos attentes en matière de qualité de tracé, vous pouvez utiliser les valeurs affichées pour `L_G` et `L_D` comme longueurs initiales pour la prochaine connexion.

# Exemples

<p align="center" width="100%">
    <img width="49%" src="https://user-images.githubusercontent.com/93446869/179190675-196e5ab6-85cf-4cc2-a4e9-f096deb4ad0e.jpg">
    <img width="49%" src="https://user-images.githubusercontent.com/93446869/179230298-3e1befce-dc5f-41f2-b96f-3180ed821823.jpg">    
</p>


# Installation

_Veuillez noter que la bibliothèque `pylgbst` nécessite l'installation de bibliothèques pour le contrôle Bluetooth comme indiqué [ici](https://github.com/undera/pylgbst/blob/master/README.md)._

Installez la bibliothèque "spiderpen" comme cela :
```bash
pip install spiderpen
```

# Disclamer

- Ce modèle reste compliqué à mettre en place d'un point de vue hardware : Il peut se décrocher, se démonter et les rubans peuvent s'emmêler. Soyez patient !
- La bibliothèque n'est pas parfaite, des bugs peuvent avoir lieu. Dans ce cas, merci de les signaler pour pouvoir les résoudre.
- Des fautes d'orthographe ou des imprécisions peuvent également se cacher dans ce dépôt. 
- Partagez les applications cool que vous avez faites ( :

# TODO

- Rédiger le fichier documentant le fonctionnement de l'algorithme de déplacement
- "Angliser" le tout

# Références

- https://www.youtube.com/watch?v=HU9SaCFnCng / https://www.youtube.com/watch?v=5x0n29MjIi8 - Les vidéos qui ont inspiré ce dépôt.
- https://github.com/undera/pylgbst - La librairie permettant le contrôle du Hub.
