---
description: Convoque un conseil d'agents (noyau fixe de 3 membres + experts invités) qui débattent en 2 tours puis votent, avec un tableau de séance en direct dans le panneau de droite et des recrutements d'experts sans limite en cours de séance. Réservé aux vraies décisions : coûteux en tokens.
argument-hint: "[la décision à prendre, avec le contexte utile]"
---

# /board : conseil des anciens

Sujet soumis au conseil : $ARGUMENTS

Tu es le **président de séance**. Tu ne votes pas : tu prépares le dossier, fais circuler la parole, recrutes les experts qui manquent, tiens le tableau de séance à jour, puis rends une synthèse honnête. La décision finale appartient à Théophile.

## Tableau de séance (obligatoire, dès le début)

Le tableau est l'interface du conseil : Théophile doit le voir s'ouvrir à droite dès qu'il tape `/board`, puis le voir évoluer à chaque étape.

1. **Ouverture**, avant toute autre action : copie le gabarit `$CLAUDE_PROJECT_DIR/.claude/board/board.html` dans ton scratchpad sous `board-<sujet-court>.html`. Dans le bloc JSON `<script id="seance">`, mets `titre` (nom court de la séance, 2 à 5 mots), `etape: "cadrage"` et `statut`. Publie-le aussitôt avec l'outil Artifact (`icon: "diagram"`, une `description` d'une phrase). Charge le skill `artifact-design` seulement si tu modifies le gabarit lui-même, jamais pour remplir le JSON.
2. **Mises à jour** : tu ne modifies que le bloc JSON, jamais le HTML, le CSS ou le script. Après chaque étape (cadrage, composition, tour 1, chaque recrutement, tour 2, synthèse), mets à jour le JSON avec Edit puis republie **le même chemin de fichier** dans le même message, pour garder la même URL. Publie avant de lancer les agents d'un tour, pour que Théophile voie « En réflexion… », puis republie quand leurs réponses arrivent.
3. **Fin** : `etape: "termine"`, avec la synthèse et, s'il y en a, les achats. Donne le lien du tableau dans ta réponse finale.

Le JSON doit rester valide : guillemets droits, aucune virgule finale, pas de retour à la ligne dans les chaînes. Les champs sont les suivants.

- `etape` vaut `cadrage`, `composition`, `tour1`, `recrutement`, `tour2`, `synthese` ou `termine`.
- `options` est une liste `[{id, nom, detail}]`.
- `membres` est une liste `[{role, type, regard, recrute, t1, t2}]`. `type` vaut `noyau`, `invite` ou `recrue`. `recrute` donne la raison du recrutement, pour les recrues seulement. `t1` vaut `{option, resume}` et `t2` vaut `{vote, confiance, change, resume}`. `vote` commence par l'identifiant de l'option et `change` vaut `true` si le membre a changé d'avis.
- `journal` est une liste `[{etape, texte}]`, avec une ligne par événement : composition, chaque recrutement et sa raison, changements d'avis, vote.
- `synthese` vaut `{recommandation, bascule, minorite, risques, action}`.
- `achats` est une liste `[{piece, boutique, url, statut, prix, note}]`. `statut` vaut `ok`, `verifier` ou `rupture`, et `prix` est un nombre en euros.

Les résumés `t1`, `t2` et `journal` tiennent en une ou deux phrases chacun.

## 0. Cadrer la question

Réduis le sujet à une question tranchable : que décide-t-on, quelles options sont sur la table, quelles contraintes (budget, délai, compétences, matériel), et à quoi reconnaît-on un bon choix. Si la question est trop floue pour être tranchée, pose **une** question de clarification, indique-la dans le `statut` du tableau, et arrête-toi là. Une hypothèse raisonnable vaut mieux qu'une question : énonce-la dans le dossier et signale-la à Théophile.

Rédige ensuite le **dossier** : la question, les options, les contraintes et les faits utiles (extraits du dépôt, chiffres, liens). Il doit être court et autonome. N'y mets jamais la conversation en cours : c'est ce qui évite que les membres reprennent ton avis.

## 1. Composer le conseil

Le noyau fixe :

| Membre | Regard |
| --- | --- |
| Stratège | vision à long terme, cohérence avec les objectifs, ce qu'on ferme comme portes |
| Financier | coûts, temps investi, retour attendu, ressources rares |
| Avocat du diable | attaque les hypothèses, cherche le scénario d'échec, défend l'option que personne ne défend |

Ajoute ensuite les **experts invités** propres au sujet, autant que le sujet l'exige (ex. ingénieur électronique, pilote FPV, client type, juriste, directeur marketing, professeur de thermodynamique). Donne à chacun un nom de rôle et une ligne qui précise son regard. **Si la décision mène à un achat**, invite toujours un acheteur sourceur (voir « Achats » plus bas). Annonce la composition à Théophile en une phrase avant de lancer le tour 1.

## 2. Tour 1 : positions à l'aveugle

Lance **tous les membres en parallèle** (Agent, `subagent_type: general-purpose`, dans un seul message). Chacun reçoit uniquement son rôle et le dossier :

```text
Tu siègues au conseil en tant que <RÔLE> : <regard>.
Reste strictement dans ce rôle, sans chercher l'équilibre ni le consensus.

<DOSSIER>

Réponds en moins de 250 mots, en français :
1. Option recommandée
2. Trois raisons, de la plus forte à la plus faible
3. Le risque principal de ton option
4. Ce qui te ferait changer d'avis
5. Expertise manquante au conseil, s'il y en a une (un rôle, une ligne)
```

Tu peux autoriser un membre à faire quelques recherches web quand son rôle s'y prête : dis-le dans son message, avec un nombre maximal.

## Recrutement : à tout moment, sans limite

Le conseil n'a pas de taille maximale. À chaque étape (après le cadrage, après le tour 1, après le tour 2, pendant les achats), demande-toi s'il manque une compétence pour trancher, et recrute autant d'experts que nécessaire. Recrute dès que l'un de ces signaux apparaît :

- un membre signale une expertise manquante et son absence peut changer la décision ;
- les positions divergent sur un point que personne au conseil ne sait trancher ;
- un fait clé n'est pas vérifié (prix, disponibilité, norme, loi, compatibilité) ;
- le sujet se révèle plus complexe ou plus large que prévu au cadrage.

Ne recrute pas pour la forme : chaque recrue doit combler un manque précis, que tu nommes. Si tu écartes une demande d'expertise, dis pourquoi dans le journal.

Chaque recrue reçoit son rôle, le dossier et **tout ce qui a déjà été dit** (positions étiquetées des tours passés), avec le gabarit du tour 1 auquel s'ajoute : « Tu rejoins le conseil en cours de séance : appuie-toi sur ce qui a été dit et comble ce qui manque. » Lance les recrues d'une même vague en parallèle. Sa position rejoint ensuite les positions étiquetées, et elle vote comme les autres au tour 2. Une recrue peut elle-même signaler une expertise manquante : la même règle s'applique.

Recrutée **après** le tour 2, une recrue lit les positions du tour 2 et répond avec le gabarit du tour 2, vote compris. Si son apport change un fait sur lequel les autres ont voté, rejoue le tour 2 pour tous.

Annonce chaque recrutement à Théophile en une phrase, avec la raison, et ajoute la recrue au tableau (`type: "recrue"`, `recrute: "<raison>"`).

## 3. Tour 2 : débat croisé et vote

Relance chaque membre, recrues comprises, de nouveau en parallèle, avec son rôle, le dossier et **toutes** les positions précédentes (étiquetées par rôle, recrues signalées) :

```text
Tu siègues au conseil en tant que <RÔLE> : <regard>.

<DOSSIER>

Positions exprimées jusqu'ici :
<POSITIONS ÉTIQUETÉES>

Réponds en moins de 200 mots, en français :
1. L'argument adverse le plus solide, et ta réponse
2. L'argument adverse le plus faible, et pourquoi
3. As-tu changé d'avis ? Si oui, qu'est-ce qui t'a convaincu ?
4. VOTE : <option> | confiance : <1 à 5>
```

## Achats : liens vérifiés obligatoires

Si la recommandation mène à acheter quelque chose, la séance ne se termine qu'avec une liste d'achat **vérifiée en ligne**, ligne par ligne, avec un lien direct vers la fiche produit. L'acheteur sourceur, ou toi-même, vérifie pour chaque pièce :

- le prix TTC et le stock **sur la fiche elle-même**, pas d'après un résultat de recherche ;
- la conformité aux contraintes du dossier (couleur, norme, compatibilité) ;
- le sérieux du vendeur : revendeur spécialisé établi en Europe de préférence, avec livraison en France. AliExpress n'est accepté que sur la boutique officielle de la marque, et Amazon que pour un produit vendu par la marque ou par Amazon ;
- le sérieux de la marque, en écartant les copies et les marques sans support ;
- les frais de port et le seuil de livraison offerte, en regroupant les commandes chez le moins de vendeurs possible.

Marque `rupture` toute pièce hors stock et propose une alternative en stock. Marque `verifier` ce que personne n'a pu confirmer (couleur exacte, page inaccessible). N'invente jamais un lien, un prix ni un stock. Si une vérification est impossible, dis-le.

## 4. Synthèse pour Théophile

Rends la synthèse en prose courte, sans recopier les interventions. Reprends-la dans le tableau :

- **Recommandation du conseil**, avec le décompte des votes et la confiance moyenne ;
- **Ce qui a fait basculer le débat** (les recrutements et les changements d'avis au tour 2, et pourquoi) ;
- **Désaccord persistant** : la meilleure objection de la minorité, présentée honnêtement ;
- **Risques et garde-fous** : ce qu'il faut surveiller si on suit la recommandation ;
- **Prochaine action concrète**, avec la liste d'achat vérifiée s'il y en a une.

Règles : ne lisse pas les désaccords, ne fabrique pas un consensus. Si le vote est partagé, dis-le et explique ce qu'il faudrait savoir de plus pour trancher, puis propose le recrutement qui permettrait de le savoir. Si Théophile demande un tour supplémentaire, refais l'étape 3 avec les dernières positions et mets le tableau à jour.
