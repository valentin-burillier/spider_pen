# Fonctionnement de l'algorithme de déplacement
## Méthode générale de déplacement

[shema de A à B]

[sheama axe]

[shema général]

[shéma transmission]

## Cinématique du système

[sheama axe]

pytagore et sa dérivée

## Zone de dessin

- poid max
- origine et sens des axesc != origine et axes de prog turtle

## Modélisation du treuil

- Lors de l’enroulement du ruban le rayon d’enroulement augmente. Ainsi, faire tourner l’axe du treuil à vitesse constante ne signifie pas que le ruban s’enroule à vitesse constante
- A chaque tour, le rayon augmente de l’épaisseur du ruban. On suppose que le rayon augmente linéairement sur un tour.

## Algorithme de correction de trajectoire

[shema de A à B]

Lors du déplacement de A à B, la position réelle du robot est bien souvent à côté de la trajectoire voulue voir figure 1. Ainsi, il semble intéressant que le robot essaye de se rapprocher de la trajectoire rectiligne entre A et B. Plus le robot est loin de la trajectoire, plus il doit compenser pour s’en rapprocher.
algo :
- On pose u le vecteur unitaire de déplacement
- On calcule le vecteur entre la position du robot et le projeté orthogonal de cette position sur (AB) (la norme de ce vecteur correspond à la distance de la position du robot à (AB)). On pondère le résultat par un coefficient dit de correction
- On ajoute ces 2 vecteurs puis on normalise le résultat

[shema champs]
