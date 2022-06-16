# Partie LEGO

Ce modèle se base à partir des pieces de l'ensemble LEGO Boost 17101. Il faut néanmoins ajouter deux vis sans fin 4716. Sans ces dernières, il n'est pas possible d'obtenir un rapport de réduction suffisant pour supporter le poid du modèle. Les instructions de montage du modèle sont disponible dans le fichier [`docs/instructions`](https://github.com/valentin-burillier/spiderpen/blob/main/docs/instructions.pdf).

[photo modèle]

# Matériels non-LEGO

Le modèle est maintenu par deux rubans bolduc de longueur 1.5m chacun. Il est possible d'utiliser des longueurs différentes si l'attribut `L_tot` est changé. La fixation avec le tableau est réalisée grâce à des ventouses. [lien vers les articles correspondant]

[photo treuil/vantouse]

Contrairement à d'autres câbles, le ruban possede des avantages :
- s'enrouler facilement
- fin, possible d'en enrouler une bonne quantité
- pas trop élastique
- de largeur compatible avec les LEGO

De plus, faire arriver les deux rubans en un même point permet au robot de toujours etre d'aplond (le robot ne se tourne pas) simplifiant le pilotage de ce dernier. Or, cela peut creer des tremblements lors du déplacement du robot. Heuresement ils ne sont pas significatif et ne perturbe pas la précision du tracé.

L'utilisation de vantouses pour la fixation est motivé par :
- s'attache et se détache facilement
- supporte le poid du robot

Les justifications de ces choix sont parfaitement détaillées dans cette vidéo : https://www.youtube.com/watch?v=5x0n29MjIi8

# Alimentation électrique

Pour cette utilisation, le Hub utilise beaucoup d'énergie. Ainsi, deux solutions sont envisageables :
- utiliser un ensemble de piles rechargeables. L'autonomie de ces dernières limite la longueur de tracé mais cela reste emplement suffisant. 
- créer une alimentation filaire du Hub. A l'aide d'un transformateur 7.5V, il est possible d'alimenter convenablement le Hub. Les batteries ne limitent donc plus le temps d'utilisation. Néanmoins, le câble d'alimentation ajoute du poid et peut géner la progression du robot.

[mettre photo du montage]
