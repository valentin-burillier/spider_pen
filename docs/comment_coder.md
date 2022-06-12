# setup

## connection

- par default bluegiga
- passer connection en arg (voir doc : undera)

## parametrage

- L_Gi, L_Di
- lenght, height : dimension tableau
- T, R, r : constantes
- L_tot : changé si besoin

# programmation

- type turtle : prog puis ça dessine
- gestion automatique de l’échelle

## dessin

- up, down : écrire
- right, left, half_turn : angle (angle ini : 0, correspond à l'horizontal vers la droite)
- forward, backward : déplacement relatif
- go_to : déplacement absolu [setx, sety]
- save_position, load_position : mémorise une position [polygone]
- change_couleur : pause dans le script pour le chgt
- show : montre le futur trajet

## fct d'action

- path : montre le trajet voulu et le trajet réalisé
- draw : execute les instructions
- finalize : remet le robot dans la position initiale
- new_drawing : efface tt

## état

- pos, position
- xcor, ycor
- isdown [write ?]

## special

- circle

## autre

- x, y : pos réel du robot
- x_min, x_max, y_min, y_max

LED :
- Bleu : att les instructions
- Vert : trace
- Jaune : changement de crayon

