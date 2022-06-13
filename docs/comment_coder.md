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

Par défaults, la direction de traçage est horizontal dirigé vers la droite. Arrivé à la position de début de traçage, le crayon se baissera automatiquement en position d'écriture.

Les LEDs du robot respecte un code couleur : 
- Bleu : le robot attend les instructions, il ne dessine pas
- Vert : le robot est en train de tracer
- Rouge : le robot attend que l'utilisateur change de crayon et appuie sur le bouton Hub (voir `change_color`)
- Orange clignotant : la batterie du robot est faible

# Mise en place
## Connection au Hub

Par default le robot essayera de se connecter au Hub via une carte Bluegiga. Pour utiliser d'autres modes de connection, veuillez vous référez à la documention fournit par le package de controle du Hub : https://github.com/undera/pylgbst

## Parametrage du robot

Le robot est caractérisé par différentes paramètres/constantes qui sont des attributs de la classe `Plotter` : 
- `L_Gi`, `L_Di` : longueurs initiales de rubans à gauche et à droite avant tout déplacement du robot
- `lenght`, `height` : dimension du tableau utilisée
- `L_tot` : longueur de ruban entre le point d'accroche et la 'bouche' du robot. Si elle est changé, il faut actualisé les paramètre grace à la méthode `calibration`
- `T` : épaisseur du ruban utilisé
- `R` : rapport de réduction (à ne pas changé)
- `r` : rayon du treuil (à ne pas changé)

# Méthodes du package spiderpen
## Dessiner

- `forward` : Avance le robot de la distance spécifiée, dans la direction où elle se dirige
- `backward` : Déplace le robot de distance dans le sens opposé à celui vers lequel elle pointe

- `right`
- `left`
- `half_turn` : angle (angle ini : 0, correspond à l'horizontal vers la droite)

- `up`
- `down` : écrire

- `go_to`
- `setx`
- `sety`

- `save_position`
- `load_position` : mémorise une position [polygone]

- `change_color` : pause dans le script pour le chgt
- `show` : montre le futur trajet

## état

- `pos` : 
- `xcor` : 
- `ycor` : 
- `isdown` : 

## fct d'action

- `path` : montre le trajet voulu et le trajet réalisé
- `draw` : execute les instructions - gestion automatique de l’échelle
- `home` : remet le robot dans la position initiale
- `new_drawing` : efface tt

## special

- `circle`
- [dot]
- [undo]

## autre

- x, y : pos réel du robot
- x_min, x_max, y_min, y_max


