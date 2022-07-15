# Introduction

Les déplacements du robot se programment en langage Logo. Les méthodes implémentées sont similaires à celles du package `turtle`. Ainsi, la programmation du robot est accessible à tout le monde. Exemple :

```python
import spiderpen as sp

p = sp.Plotter(lenght=820, height=1140)

n, T = 7, 4
for _ in range(n):
    p.forward(100)
    p.left(360/n*T)
p.up()

# p.show()

p.connect(L_Gi=890, L_Di=825)

p.draw(fill_factor=0.8)

p.path()

p.home()
p.disconnect()
```

<p align="center" width="100%">
    <img width="40%" src="https://user-images.githubusercontent.com/93446869/178950454-94ffe558-e88c-4e73-b338-450970c48cd0.jpg">
    <img width="58%" src="https://user-images.githubusercontent.com/93446869/178952035-65015931-258d-48f9-a37a-f8c4723cc1c7.png">
    <em>Photo du dessin réel et graphique afficher par path</em>
</p>

Le détail des méthodes utilisées est décrit dans cette [section](#Méthodes-du-package-spiderpen).

Pour faciliter l'envoi des instructions au robot, il est conseillé d'utiliser une interface de programmation en cellule telle que Jupyther Lab (Jupyther Notebook, Spyder (avec #%%)... peuvent être utilisés).

En fonctionnement, la LED du robot respecte un code couleur : 
- Bleu : Le robot attend les instructions, il ne dessine pas.
- Vert : Le robot est en train de tracer.
- Rouge : Le robot attend que l'utilisateur change de crayon et appuie sur le bouton Hub (voir `change_color`).
- Orange clignotant : La batterie du robot est faible.

# Mise en place
## Paramétrage du robot

Le robot est caractérisé par différents paramètres/constantes qui sont des attributs de la classe `Plotter` : 
- `L_Gi`, `L_Di` : Longueurs initiales des rubans à gauche et à droite avant tout déplacement du robot. Ces paramètres sont nécessaires pour établir l'étalonnage.
- `lenght` : Distance séparant les deux ventouses.
- `height` : Hauteur du tableau utilisée.
- `L_tot` : Longueur de ruban entre la ventouse et les deux rouleaux côte à côte du robot. Elle est fixée à 1.5 m.
- `T` : Épaisseur du ruban utilisée. Celle paramétrée correspond à un ruban standard.
- `R` : Rapport de réduction entre l'arbre moteur et le treuil.
- `r` : Rayon du treuil.

## Position initiale

Lors de l'initialisation d'un objet `Plotter` les paramètres `lenght` et `height` exprimé en millimètres sont à renseigner.

Le robot doit avoir son stylo en position levé en position initiale.

Par défaut, la direction de traçage est horizontale, dirigée vers la droite correspondant à un angle de 0°. Arrivé à la position de début de traçage, le stylo se baissera automatiquement en position d'écriture.

L'utilisateur doit réaliser la mesure de `L_Gi` et `L_Di` pour les paramétrer lors de la connexion au Hub. `home` permet de remettre le robot dans la position initiale afin que l'utilisateur n'ait pas besoin d'effectuer la mesure à chaque fois.

<p align="center" width="100%">
    <img width="50%" src="https://user-images.githubusercontent.com/93446869/179193353-4bf74dee-e1a4-4076-a1b0-fb0bdf69f68f.jpg">
</p>

## Connexion au Hub

Par defaut, le robot essayera de se connecter au Hub via une carte Bluegiga. Pour utiliser d'autres modes de connexion, veuillez vous référer à la documentation fournie par [le package de contrôle du Hub](https://github.com/undera/pylgbst).

La connexion est gérée par la méthode `connect` qu'il est possible d'appeler uniquement au moment du traçage. Ainsi, l'utilisateur peut planifier sont tracé avant de connecter le Hub.

`disconnect` permet de déconnecter le Hub.

# Méthodes du package spiderpen

Cette documentation est fortement inspirée de celle de [`turtle`](https://docs.python.org/fr/3/library/turtle.html).

Les instructions de dessin ne sont pas exécutées immédiatement. Il faut utiliser la méthode `draw` pour exécuter la suite d'instructions qui a été préalablement créée. Cela permet un bon calibrage du tracer dans la zone de dessin.

## Déplacer et dessiner

- `clear` : Réinitialisation de la suite d'instructions, les coordonnées sont remises à (0, 0), l'angle à 0°, le stylo se baissera automatiquement après le premier déplacement
- `undo` : Enlève la dernière instruction réalisée (up, setx, change_color,...). Ne fonctionne pas avec : left, right, half_turn, setheading, circle. [à amliorer]
- `up` : Lève le stylo
- `down` : Baisse le stylo
- `forward` : Avance le robot de la distance spécifiée, dans la direction où elle se dirige
- `backward` : Déplace le robot de distance dans le sens opposé à celui vers lequel elle pointe
- `right` : Tourne le robot à droite (sens horaire) de `angle` exprimer en degrés
- `left`  : Tourne le robot à gauche (sens antihoraire) de `angle` exprimer en degrés
- `half_turn` : Tourne le robot de 180°
- `goto` : Déplace le robot vers une position absolue. Ne change pas l'orientation du robot
- `setx` : Définit la coordonnée en x du robot, en laissant celle en y inchangé
- `sety` : Définit la coordonnée en y du robot, en laissant celle en x inchangé
- `setheading` : Définit l'orientation absolue du robot
- `circle` : Dessine un cercle de rayon `radius`. Le signe de `radius` détermine si le cercle est tracé à gauche ou à droite. Si `radius>0` le centre du cercle est gauche sinon il est à droite. Le centre du cercle se situe à la distance de `radius` par rapport à la position actuelle du robot et perpendiculairement à l'orientation du robot. `angle` détermine sur quelle portion de cercle va être tracé. Si `angle=90`, un quart de cercle sera tracé. `n` et `d_max` permettent de régler le niveau de détail du cercle.
- `change_color` : Effectue une pause dans le script : le stylo est levé, la LED du Hub passe au rouge, l'utilisateur peut changer de stylo, la suite du script continue en appuyant sur le bouton du Hub, le stylo revient dans l'état qu'il était auparavant.

## État du robot

- `pos` : Renvoie la position actuelle du robot
- `xcor` : Renvoie la coordonnée actuelle selon x du robot
- `ycor` : Renvoie la coordonnée actuelle selon y du robot
- `isdown` : Renvoie `True` si le stylo est baissé et `False` sinon
- `heading` : Renvoie l'orientation du robot. L'attribut correspondant est `angle`
- `show` : Montre le futur trajet que va emprunter le robot

## Execution d'instructions

- `connect` : Permet de connecter le robot. Si `hub=None`, cela exécutera une tentative de connexion via la carte Bluegiga. Il est possible de le connecter d'autres manières en lui passant comme argument un objet de type Movehub. Plus d'info [ici](https://github.com/undera/pylgbst/blob/master/README.md). Il faut également renseigner les longueurs initiales des rubans `L_Gi` et `L_Di` en millimètres. S'ils sont égales à None, les dernières valeurs de longueurs des rubans seront utilisées.
- `disconnect` : Déconnecte le robot.
- `path` : affiche un graphique matplotlib avec le trajet demandé par l'utilisateur et le trajet qui a été mesurer par le Hub.
- `home` : Déplace le robot à la position initiale. Ainsi, l'utilisateur n'a pas besoin d'effectuer la mesure de `L_Gi` et `L_Di` à chaque fois.
- `draw` : Exécute les instructions de dessin préalablement choisi. Par defaut, la gestion de l'échelle est automatique, c'est-à-dire que le dessin est centré et occupe 100% de la zone de dessin. L'argument `center` permet de centrer le tracé dans la zone de dessin. Si `center=True`, le robot commencera le tracé pour qu'il soit centré dans la zone de dessin, si `center=False`, le tracé partira du centre de la zone correspondant à l'origine. L'argument `fill_factor` correspond au taux de remplissage du tracé dans la zone de dessin. Si `fill_factor=0.6` le tracé remplira 60% de la zone de dessin. S'il est égal à zéro le tracé sera mis à l'échelle : les coordonnées d'instruction sont exprimées en millimètres.

<p align="center" width="100%">
    <img width="50%" src="https://user-images.githubusercontent.com/93446869/175830789-4be04a68-29c5-45fe-abc7-aa7e20859aa6.png">    
</p>
