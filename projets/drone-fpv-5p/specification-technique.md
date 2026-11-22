# Drone FPV 5 pouces analogique : spécification chiffrée (phase 1)

Conseiller technique et scientifique, 22/11/2026. Masses et poussées : ordres de grandeur de fiches constructeur, à confirmer par Stratégie sur la variante achetée. Aucun prix ici, hors ceux relevés dans le dossier.

## Spécification par poste

| Poste | Spécification | Masse retenue |
|---|---|---|
| Châssis | 5 pouces, carbone noir, empattement 220 à 230 mm, bras de 5 à 6 mm (charge lourde), montage stack 30,5 mm, caméra 19 mm, place pour une antenne VTX en SMA/UFL arrière | 120 g |
| Moteurs ×4 | 2207 ou 2306, 6S, **1750 à 1850 KV** (1950 KV chauffe sous charge lourde), arbre 5 mm. Réf. dossier : XING2 2207, 31,6 g avec câbles, 35 A crête, 842 W max (manuel iFlight) | 126 g |
| Stack 30,5 mm | FC F405 Betaflight + ESC 4-en-1, **55 à 60 A** continu, 3 à 6S, au moins 2 UART libres (RX CRSF + VTX SmartAudio/Tramp), OSD analogique. Réf. : SpeedyBee F405 V4 55A/60A | 25 g |
| VTX | Analogique 5,8 GHz, **48 canaux dont bande R**, palier **25 mW** réel, pit mode, contrôle SmartAudio ou IRC Tramp, antenne circulaire de **même polarisation que le casque** | 13 g |
| Caméra | Analogique 19 mm, **4:3** ou commutable 4:3/16:9, 4,5 à 25 V | 8 g |
| Récepteur | ExpressLRS 2,4 GHz type RP3 (SX1281, CRSF), antenne T ou dipôle | 2 g |
| Hélices | 5 pouces tripales 5×4,3×3 ou 51466, noires ; prévoir 3 à 4 jeux | 18 g |
| Divers | Câble XT60 12 AWG, condensateur 35 V 1000 µF, visserie, strap | 20 g |
| **Drone sec** | | **≈ 332 g** |
| Batteries ×2 | **LiPo 6S1P, XT60, 1300 à 1800 mAh**, ≥ 100C annoncé, coque noire ou noire et rouge. Vérifier que le chargeur de Théophile gère le 6S | 215 g (1300) à 290 g (1800) |

## Performances calculées

Hypothèses : poussée 1,4 kg par moteur en 6S avec hélice 5 pouces (valeur prudente pour un 2207 de ce KV, non trouvée sur la fiche XING2, à confirmer), théorie de Froude, figure de mérite 0,55, rendement moteur+ESC 0,78, croisière ≈ 1,8 fois la puissance de vol stationnaire, 80 % de la capacité utilisable. Le modèle est optimiste de 20 à 30 % en vol réel ; les durées ci-dessous en tiennent compte.

| Batterie | Charge | Masse en vol | Poussée/poids | Croisière |
|---|---|---|---|---|
| 6S 1300 | 0 g | 547 g | 10,2 | ≈ 6 à 8 min |
| 6S 1300 | 300 g | 847 g | 6,6 | ≈ 4 min |
| 6S 1300 | 600 g | 1 147 g | 4,9 | ≈ 2,5 min |
| 6S 1800 | 0 g | 622 g | 9,0 | ≈ 8 à 10 min |
| 6S 1800 | 300 g | 922 g | 6,1 | ≈ 5 min |
| 6S 1800 | 600 g | 1 222 g | 4,6 | ≈ 3 min |
| Li-ion 6S 4000 | 300 g | 1 052 g | 5,3 | ≈ 9 min (courant limité, pas de freestyle) |

Charge utile maximale pilotable (poussée/poids ≥ 4) : environ 800 g avec une 1300, 700 g avec une 1800. Le courant reste sous les 55 A par ESC (35 A crête moteur). **Les 10 minutes ne sont tenables qu'à vide, en vol tranquille, avec une 6S 1800.** Avec charge, compter 3 à 5 min.

## Portée réaliste à 25 mW

Bilan de liaison vidéo : PIRE 14 dBm, perte en espace libre à 5,8 GHz, 1 dB de pertes, sensibilité du SKY04X Pro −98 dBm, image propre vers −90 dBm.

| Distance | Antenne omni 2 dBi | Patch 8 dBi |
|---|---|---|
| 300 m | marge 8 dB | marge 14 dB |
| 500 m | marge 3 dB | marge 9 dB |
| 1 km | image dégradée | marge 3 dB |
| 1,5 km | neige | limite |

La portée vidéo réaliste est donc de **300 à 500 m avec les antennes d'origine, 800 m à 1 km avec un patch**, en vue directe. Le lien radio ELRS (100 mW, 50 Hz) dépasse 10 km : c'est la vidéo qui limite. « Plusieurs kilomètres » est impossible à 25 mW.

## Compatibilité

**RadioMaster Pocket ELRS.** Module ELRS 2,4 GHz interne, CRSF. Le RP3 doit être en **même version majeure d'ExpressLRS (3.x)** et avec la même phrase de bind. En France, la radio 2,4 GHz est limitée à **100 mW PIRE** : régler la Pocket à 100 mW au plus (elle monte à 250 mW). Le script Lua ELRS « VTX Admin » règle canal et puissance du VTX depuis la Pocket si le VTX est piloté par SmartAudio ou Tramp. Certitude élevée.

**SKY04X Pro.** Récepteur SteadyView 48 canaux (A, B, E, F, R, L), sensibilité −98 dBm, connecteurs SMA femelle, deux antennes 2 dBi fournies dont la polarisation n'est pas publiée. Deux points à faire vérifier par Théophile : **la polarisation (RHCP ou LHCP) de ses antennes**, à reprendre sur le VTX, et le format d'image (4:3 par défaut sur la gamme SKY04X, 16:9 natif selon un test du Pro ; une caméra commutable lève le doute).

**Canaux légaux** (bande 5 725 à 5 875 MHz, 25 mW PIRE) : R3 5 732, R4 5 769, R5 5 806, R6 5 843 MHz, ainsi que les canaux A, B, E et F compris dans cette plage. R1, R2, R8 et la bande L sont hors bande. Verrouiller la table VTX de Betaflight sur ces canaux et sur 25 mW.

## Arbitrages à soumettre à Théophile

1. **Portée contre légalité.** À 25 mW, la vidéo tient 0,5 à 1 km ; au-delà il faut 200 à 800 mW, illégal en France. De plus, en catégorie ouverte, le vol en immersion exige un observateur gardant le drone en vue : la portée légale est de quelques centaines de mètres de toute façon. Recommandation : rester légal, ajouter un patch sur le casque plus tard.
2. **Charge contre autonomie.** Batteries 6S 1300 (plus agiles, ≈ 6 à 8 min à vide) ou 6S 1800 (≈ 8 à 10 min à vide, 3 à 5 min chargé). Recommandation : 6S 1800 si l'objectif est la charge et les 10 min, 1300 si c'est le pilotage.
3. **Enregistrement.** Le drone dépasse 250 g (≈ 550 à 620 g à vide) : enregistrement de l'exploitant sur AlphaTango, numéro sur le drone, formation en ligne A1/A3. L'enregistrement est de toute façon dû dès qu'il y a une caméra. Au-delà de 800 g avec charge, le signalement électronique peut être exigé (règle à confirmer par le spécialiste réglementation). Alternative : voler en club d'aéromodélisme. Question à Théophile : accepte-t-il ces démarches, ou faut-il plafonner la masse ?

## Sources

[Manuel iFlight XING2 2207 1855KV](https://www.rotorama.com/assets/docs/a7096414bfd47dcb0cecd5ae9a9d2967/46280-1/iflight-xing2-2207-1855kv-manual-en.pdf), [fiche XING2 2207 (GetFPV)](https://www.getfpv.com/motors/mini-quad-motors/iflight-xing2-2207-motor-1855kv-2755kv.html), [test SKY04X Pro (Oscar Liang)](https://oscarliang.com/skyzone-sky04x-pro), [fiche SKY04X Pro (GetFPV)](https://www.getfpv.com/skyzone-sky04x-pro-fpv-goggles-black.html), [manuel SKY04X Pro](https://www.bezpeka-shop.com/download/manuals/sky04x-pro-manual-eng.pdf). Calculs : modèle de Froude et perte en espace libre, script Python du conseiller.
