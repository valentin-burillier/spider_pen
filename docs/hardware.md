# Partie LEGO

Liste de matériels :
- [LEGO Boost 17101](https://www.lego.com/fr-fr/product/boost-creative-toolbox-17101)
- [2 vis sans fin 4716](https://www.toypro.com/fr/product/17870/technique-equipement-vis-sans-fin/blanc?gclid=CjwKCAjw_b6WBhAQEiwAp4HyIPGTKaxt4KpYFZgB9HFoquSJDSgadKyJU93lJmsSK07TIOHpsYwnxBoCSOEQAvD_BwE)

Ce modèle se base à partir des pieces de l'ensemble LEGO Boost 17101. Il faut néanmoins ajouter deux vis sans fin 4716. Sans ces dernières, il n'est pas possible d'obtenir un rapport de réduction suffisant pour supporter le poid du modèle. Les instructions de montage du modèle sont disponible dans le fichier [docs/instructions](https://github.com/valentin-burillier/spiderpen/blob/main/docs/instructions.pdf).

[photo modèle]

Les pattes noires à l'avant n'ont pas seulement un but décoratif. Ils permettent au robot de ne pas pivoter autour de l'axe verticale lors du tracé.

Les pieces oranges à coté des yeux peuvent être pivoter afin de déconnecter les treuils de leur vis sans fin. Cela permet de régler manuellement la longueur des câbles.

# Partie non-LEGO

Liste de matériels :
- [Ruban bolduc](https://www.amazon.fr/Clairefontaine-601775C-Bolduc-500mx7mm-Couleur/dp/B001ANX5DA/ref=pd_day0_sccl_3_1/257-8157104-5120103?pd_rd_w=3biio&content-id=amzn1.sym.5a3d874f-f0eb-4ad9-ac25-35518704bcec&pf_rd_p=5a3d874f-f0eb-4ad9-ac25-35518704bcec&pf_rd_r=DCW3MXNY52EPCRZQH4VQ&pd_rd_wg=TKBIy&pd_rd_r=16b9b116-07db-4bf9-9941-8449467ff04f&pd_rd_i=B001ANX5DA&th=1)
- [2 vantouses de 45mm](https:///Nuenen-Ventouses-Transparentes-Champignon-Extérieur/dp/B09MVLSN4M/ref=mp_s_a_1_16)
- [Feutres](https:///BIC-Velleda-1741-Feutres-Effaçables/dp/B001AS5FHO/ref=mp_s_a_1_7)
- [Tableau blanc](https:///Eco-magnétique-Tableau-blanc-120/dp/B00P7XD27S/ref=mp_s_a_1_9)
- [Carte Bluegiga](https://www.silabs.com/wireless/bluetooth/bluegiga-low-energy-legacy-modules/device.bled112) (si Windows)

Le modèle est maintenu par deux rubans bolduc de longueur 1.6m chacun. La fixation avec le tableau est réalisée grâce à des ventouses.

Contrairement à d'autres câbles, le ruban possede des avantages :
- s'enrouler facilement
- fin, possible d'en enrouler une bonne quantité
- pas trop élastique
- de largeur compatible avec les LEGO

De plus, faire arriver les deux rubans en un même point permet au robot de toujours etre d'aplond (le robot ne se tourne pas) simplifiant le pilotage de ce dernier. Or, cela peut creer des tremblements lors du déplacement du robot. Heuresement ils ne sont pas significatif et ne perturbe pas la précision du tracé.

Les vantouses permettent de :
- supporter le poid du robot
- s'attacher et se détacher facilement du tableau

De part la conception du modèle, tous les types de feutre ne peuvent pas être utilisés.

Les justifications de ces choix sont parfaitement détaillées dans cette [vidéo](https://www.youtube.com/watch?v=5x0n29MjIi8).

# Alimentation électrique

Liste de matériels :
- [Transformateur](https://www.amazon.fr/Zolt-international-dalimentation-haut-parleurs-%C3%A9lectroniques/dp/B0932FLPX4/ref=sr_1_1_sspa?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=24HWBCWFTJQVY&keywords=transformateur+9v&qid=1657815146&sprefix=transformateur+9v%2Caps%2C109&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNUVSWTBWMFZUQVVSJmVuY3J5cHRlZElkPUEwMDM2NDQ5MTdMSFUwRlNIVENJMSZlbmNyeXB0ZWRBZElkPUEwMDM2OTYxMUhRV0w0V01LQzZHVCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=)

Pour cette utilisation, le Hub utilise beaucoup d'énergie. Ainsi, il est conseillé de créer une alimentation filaire.

A l'aide d'un transformateur 7.5-9V, il est possible d'alimenter convenablement le Hub. Les batteries ne limitent donc plus le temps d'utilisation. Se référer [ici](https://www.youtube.com/watch?v=iMCDWRqhlA8).

Pour les personnes disposant d'une imprimante 3D, voici un [adaptateur](https://cults3d.com/fr/mod%C3%A8le-3d/jeu/lego-boost-move-hub-power-adapter) à imprimer.
