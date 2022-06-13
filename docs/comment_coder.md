# Introduction

Les déplacements du robot se programment en langage Logo. Les méthodes implémentées sont similaires à celle du package turtle. Ainsi, la programmation du robot est accessible à tout le monde. Exemple :

```python
import spiderpen as sp

p = sp.Plotter(lenght=0.813, height=1.15, L_Gi=0.63, L_Di=0.835)

n, T = 20, 9
for _ in range(n):
    p.forward(100)
    p.left(360/n*T)
p.up()

p.draw()
p.home()
```

[mettre photo path et reel]

La LED du robot respecte un code couleur : 
- Bleu : le robot attend les instructions, il ne dessine pas
- Vert : le robot est en train de tracer
- Rouge : le robot attend que l'utilisateur change de crayon et appuie sur le bouton Hub (voir `change_color`)
- Orange clignotant : la batterie du robot est faible

# Mise en place
## Connection au Hub

Par default le robot essayera de se connecter au Hub via une carte Bluegiga. Pour utiliser d'autres modes de connection, veuillez vous référez à la documention fournit par le package de controle du Hub : https://github.com/undera/pylgbst

## Parametrage du robot

Le robot est caractérisé par différentes paramètres/constantes qui sont des attributs de la classe `Plotter` : 
- `L_Gi`, `L_Di` : longueurs initiales des rubans à gauche et à droite avant tout déplacement du robot
- `lenght`, `height` : dimension du tableau utilisée
- `L_tot` : longueur de ruban entre le point d'accroche et la 'bouche' du robot. Si elle est changé, il faut actualisé les paramètres grace à la méthode `calibration`
- `T` : épaisseur du ruban utilisé
- `R` : rapport de réduction entre l'arbre moteur et le treuil (à ne pas changé)
- `r` : rayon du treuil (à ne pas changé)

## Position initiale

L'utilisateur doit réalisé la mesure de `L_Gi` et `L_Di` pour les paramétrer lors de l'initialisation du Hub. `home` permet de remettre le robot dans la position initiale afin que l'utilisateur n'est pas besoin d'effectuer la mesure à chaque fois.

Le robot doit avoir son stylo en position levé en position initiale.

Par défaults, la direction de traçage est horizontal dirigé vers la droite correspondant à un angle de 0°. Arrivé à la position de début de traçage, le stylo se baissera automatiquement en position d'écriture.

# Méthodes du package spiderpen

Cette documentation est fortement inspirer de cellede turtle : https://docs.python.org/fr/3/library/turtle.html

Les instructions de dessin ne sont pas executer imédiatement. Il faut utiliser la méthode `draw` pour executer la suite d'instruction qui a été préalablement créée. Cela permet un bon calibrage du tracer dans la zone de dessin.

## Déplacer et dessiner

- `new_drawing` : réinitialisation de la suite d'instruction, les coordonnées sont remises à (0, 0), l'angle à 0°, le stylo se baissera automatiquement apres le premier déplacement
- [undo]
- `up` : Lève le stylo
- `down` : Baisse le stylo
- `forward` : Avance le robot de la distance spécifiée, dans la direction où elle se dirige
- `backward` : Déplace le robot de distance dans le sens opposé à celui vers lequel elle pointe
- `right` : Tourne le robot à droite (sens horraire) de `angle` exprimer en degres
- `left`  : Tourne le robot à gauche (sens anti-horraire) de `angle` exprimer en degres
- `half_turn` : Tourne le robot de 180°
- `go_to` : Déplace le robot vers une position absolue. Ne change pas l'orientation du robot
- `setx` : Définit la coordonnée en x du robot, en laissant celle en y inchangé
- `sety` : Définit la coordonnée en y du robot, en laissant celle en x inchangé
- `setheading` : Définit l'orienttion absolue du robot
- `save_position` : mémorise la position actuelle du robot
- `load_position` : déplace le robot à la dernière position sauver. Ne change pas l'orientation du robot
- [gestion des polygones : begin_shape, end_shape, turn_shape_ clone...]
- `circle` : Dessine un cercle de rayon `radius`. Le signe de `radius` détermine si le cercle est tracé à gauche ou à droite. Le centre du cercle se situe à la distance de `radius` par rapport à la position actuelle du robot et perpendiculairement à l'orientation du robot. `angle` détermine quel est la portion de cercle qui va être dessinée. Si `angle=90`, un quart de cercle sera tracé. `n` et `d_max` permette de régler le niveau de détail du cercle. [à détailler]
- `change_color` : effectue une pause dans le script : le stylo est levé, la LED du Hub passe au rouge, l'utilisateur peut changer de stylo, la suite du script continue en appuyant sur le bouton du Hub, le stylo revient dans l'état qu'il était auparavant

## État du robot

- `pos` : renvoie la position actuelle du robot
- `xcor` : renvoie la coordonnée actuelle selon x du robot
- `ycor` : renvoie la coordonnée actuelle selon y du robot
- `isdown` : renvoie `True` si le stylo est baissé et `False` sinon
- `heading` : renvoie l'orientation du robot. L'attribut correspondant est `angle`
- `show` : montre le futur trajet que va empreinter le robot

## Execution d'instructions

- `calibration` : permet de définir la zone de dessin et les différents paramètres du robot
- `path` : affiche un graphique matplotlib avec le trajet demandé par l'utilisateur et le trajet qui a été mesurer par le Hub
- `home` : Déplace le robot à la position initiale
- `draw` : Execute les instructions de dessin préalablement choisit. Par default, la gestion de l'échelle est automatique, c'est à dire que le dessin est centrer et occupe 90% de la zone de dessin. L'argument `center` permet de centrer le tracer dans la zone de dessin. Si `center=True`, le robot commencera le tracer pour qu'il soit centrer dans la zone de dessin, si `center=False`, le tracer partira du centre de la zone de dessin correspondant à l'origine. L'argument `fill_factor` correspond au taux de remplissage du tracer dans la zone de dessin. Si `fill_factor=0.6` le tracer remplira 60% de la zone de dessin, s'il est égale à zero le tracer sera mis à l'échelle. Alors, les coordonnées d'instruction sont exprimer en milimètre. [mettre shema 4 cadrants de la differences entre les paramètres]
