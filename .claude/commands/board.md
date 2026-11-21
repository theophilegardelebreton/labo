---
description: Convoque un conseil d'administration d'agents (noyau fixe de 3 membres + 1 à 3 experts invités selon le sujet) qui débattent en 2 tours puis votent, pour aider Théophile à prendre une décision. Réservé aux vraies décisions : coûteux en tokens.
argument-hint: "[la décision à prendre, avec le contexte utile]"
---

# /board : conseil des anciens

Sujet soumis au conseil : $ARGUMENTS

Tu es le **président de séance**. Tu ne votes pas : tu prépares le dossier, fais circuler la parole, puis rends une synthèse honnête. La décision finale appartient à Théophile.

## 0. Cadrer la question

Réduis le sujet à une question tranchable : que décide-t-on, quelles options sont sur la table, quelles contraintes (budget, délai, compétences, matériel), et à quoi reconnaît-on un bon choix. Si la question est trop floue pour être tranchée, pose **une** question de clarification et arrête-toi là.

Rédige ensuite le **dossier** : la question, les options, les contraintes et les faits utiles (extraits du dépôt, chiffres, liens). Il doit être court et autonome. N'y mets jamais la conversation en cours : c'est ce qui évite que les membres reprennent ton avis.

## 1. Composer le conseil

Le noyau fixe :

| Membre | Regard |
| --- | --- |
| Stratège | vision à long terme, cohérence avec les objectifs, ce qu'on ferme comme portes |
| Financier | coûts, temps investi, retour attendu, ressources rares |
| Avocat du diable | attaque les hypothèses, cherche le scénario d'échec, défend l'option que personne ne défend |

Ajoute ensuite **1 à 3 experts invités** propres au sujet (ex. ingénieur électronique, pilote FPV, client type, juriste, directeur marketing, professeur de thermodynamique). Donne à chacun un nom de rôle et une ligne qui précise son regard. Annonce la composition à Théophile en une phrase avant de lancer le tour 1.

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
```

## 3. Tour 2 : débat croisé et vote

Relance chaque membre, de nouveau en parallèle, avec son rôle, le dossier et **toutes** les positions du tour 1 (étiquetées par rôle) :

```text
Tu siègues au conseil en tant que <RÔLE> : <regard>.

<DOSSIER>

Positions du premier tour :
<POSITIONS ÉTIQUETÉES>

Réponds en moins de 200 mots, en français :
1. L'argument adverse le plus solide, et ta réponse
2. L'argument adverse le plus faible, et pourquoi
3. As-tu changé d'avis ? Si oui, qu'est-ce qui t'a convaincu ?
4. VOTE : <option> | confiance : <1 à 5>
```

## 4. Synthèse pour Théophile

Rends la synthèse en prose courte, sans recopier les interventions :

- **Recommandation du conseil**, avec le décompte des votes et la confiance moyenne ;
- **Ce qui a fait basculer le débat** (les changements d'avis au tour 2, et pourquoi) ;
- **Désaccord persistant** : la meilleure objection de la minorité, présentée honnêtement ;
- **Risques et garde-fous** : ce qu'il faut surveiller si on suit la recommandation ;
- **Prochaine action concrète**.

Règles : ne lisse pas les désaccords, ne fabrique pas un consensus. Si le vote est partagé, dis-le et explique ce qu'il faudrait savoir de plus pour trancher. Si Théophile demande un tour supplémentaire, refais l'étape 3 avec les positions du tour 2.
