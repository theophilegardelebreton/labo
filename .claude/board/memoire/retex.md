# Retours d'expérience du conseil

Le Directeur général relit ce fichier au début de chaque séance `/board` et en applique les leçons. À la fin d'une séance, il ajoute au plus trois lignes : l'expert qui a manqué, l'erreur à ne pas refaire, ce qui a bien marché.

- Les prix, stocks et coloris donnés de mémoire par les agents se sont révélés faux plusieurs fois. Il faut toujours les vérifier sur la fiche produit, et recruter un acheteur sourceur dès qu'une décision mène à un achat.
- Pour tout matériel qui émet (vidéo, radio), il faut rappeler les limites légales en France dès le cadrage : un spécialiste de la réglementation a changé la liste de pièces.
- Relancer de nouveaux agents au tour 2 a coûté environ 80 000 tokens de contexte chacun. Il faut continuer les agents existants avec SendMessage.
- Deux experts recrutés après le tour 1, demandés chacun par deux membres, ont fait bouger le chiffrage et la liste de pièces. Le recrutement en cours de séance est utile.
- Les outils de lecture web génériques lisent mal les boutiques en ligne : relever prix et stock dans les données structurées de la fiche (JSON-LD) et chercher les produits dans le sitemap de la boutique. Un spécialiste léger équipé de ce relevé devient fiable.
- Vérifier le prix et le stock de la variante choisie (coloris, KV, taille), pas le prix d'appel de la fiche : la relecture finale par le comité a ainsi corrigé un total.
- Quand un opposant pose une condition vérifiable pour changer d'avis, la remplir par des faits sourcés tranche mieux qu'un nouveau face-à-face.
