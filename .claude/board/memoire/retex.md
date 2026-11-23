# Retours d'expérience du conseil

Le Directeur général relit ce fichier au début de chaque séance `/board` et en applique les leçons. À la fin d'une séance, il ajoute au plus trois lignes : l'expert qui a manqué, l'erreur à ne pas refaire, ce qui a bien marché.

- Les prix, stocks et coloris donnés de mémoire par les agents se sont révélés faux plusieurs fois. Il faut toujours les vérifier sur la fiche produit, et recruter un acheteur sourceur dès qu'une décision mène à un achat.
- Pour tout produit soumis à une réglementation (émissions, sécurité, normes), il faut rappeler les limites légales dès le cadrage : un spécialiste de la réglementation a déjà changé une liste d'achat.
- Relancer de nouveaux agents au tour 2 a coûté environ 80 000 tokens de contexte chacun. Il faut continuer les agents existants avec SendMessage.
- Deux experts recrutés après le tour 1, demandés chacun par deux membres, ont fait bouger le chiffrage et la liste de pièces. Le recrutement en cours de séance est utile.
- Les outils de lecture web génériques lisent mal les boutiques en ligne : relever prix et stock dans les données structurées de la fiche (JSON-LD) et chercher les produits dans le sitemap de la boutique. Un spécialiste léger équipé de ce relevé devient fiable.
- Vérifier le prix et le stock de la variante choisie (couleur, taille, version), pas le prix d'appel de la fiche : la relecture finale par le comité a ainsi corrigé un total.
- Quand un opposant pose une condition vérifiable pour changer d'avis, la remplir par des faits sourcés tranche mieux qu'un nouveau face-à-face.
- Quand l'outil de lecture web d'un spécialiste échoue sur une boutique (boucle de redirections, refus), relever soi-même prix et stock en ligne de commande dans le balisage de la fiche (microdata `itemprop`, couche de données de suivi) plutôt que relancer l'agent : c'est rapide et fiable.
- En période de soldes, le prix d'appel des métadonnées peut différer du prix courant : retenir le prix effectivement facturé, vérifier le stock de chaque variante (couleur, KV, taille) et signaler que le prix est temporaire.
- Faire voter sur des paniers déjà vérifiés et chiffrés plutôt que sur des architectures abstraites : les écarts réels de prix et de stock ont fait bouger des votes que les débats n'avaient pas fait bouger.
- Toute question ou correction posée après la synthèse, dans la même conversation, repasse par le conseil : le DG rouvre la séance (nouvelle séance du même projet, sur la base déjà acquise), injecte les faits nouveaux, recrute si un manque apparaît, fait revoter, puis répond. Le DG ne tranche jamais seul une révision de livrable, même petite (couleur, pièce, budget) ; il peut ajouter les étapes utiles et décide sans solliciter le demandeur sauf impasse réelle.
- Vérifier sur les photos des fiches la couleur réelle de chaque pièce visible quand un code couleur est imposé : une étiquette de batterie jaune vif est passée inaperçue jusqu'à la relecture.
