---
description: Clôture le projet en cours du conseil pour repartir de zéro en gardant l'organisation. Enregistre les leçons, ferme le tableau, puis rappelle de taper /clear, qui efface les sous-agents avec la conversation.
argument-hint: "(aucun argument)"
---

# /fin : clôturer le projet

Théophile a décidé de clôturer le projet en cours. Tu es le Président (`.claude/commands/president.md`).

0. **Améliorations du conseil.** Si le Président n'a pas encore proposé d'améliorations du conseil pour ce projet (étape « 7. Synthèse » de `president.md`), fais-le maintenant et attends la réponse de Théophile. Applique ensuite celles qu'il a acceptées : fiches de `.claude/conseil/annuaire/` (ajout, retrait, spécialisation), protocoles (`president.md`, `conseiller.md`, `controle.md`, `outils.md`, `catalogue.md`), gabarits de tableau (`.claude/conseil/president.html`, `.claude/board/board.html`, en ne touchant qu'au bloc JSON par défaut et au code utile, puis en vérifiant le rendu dans un navigateur) ou skills. Pour une modification des tableaux ou des protocoles, fais relire la modification par le Head of Common Sense. Passe chacune à `appliquee`. Si un conseiller de base est ajouté ou retiré, mets aussi à jour « Équipe en veille » dans `president.md` et l'équipe par défaut du tableau.
1. **Clôture.** Applique l'étape « 8. Clôture » de `.claude/commands/president.md` : leçons générales des conseillers et du Head of Common Sense, section « Leçons » des fiches, `retex.md`, nouvelles fiches, skills qui ont fait leurs preuves et améliorations acceptées à l'étape 0, publiés ensemble dans la branche par défaut. Théophile a autorisé cette fusion pour ces fichiers du conseil (`.claude/conseil/`, `.claude/commands/president.md`, `.claude/commands/fin.md`, `.claude/board/`, `.claude/skills/`, `.claude/skills-off/`). Si aucun projet n'est en cours dans cette conversation, saute cette étape et dis-le en une phrase.
2. **Arrêter l'équipe.** Si des sous-agents tournent encore, arrête-les avec TaskStop. N'en continue aucun : le prochain projet repart de sous-agents neufs.
3. **Tableau.** Passe le tableau du projet à `phase: "terminé"`, avec un `statut` et un `point.etat` qui disent que le projet est clos, puis republie-le : il reste consultable dans les artefacts. Le prochain projet ouvrira un tableau vierge.
4. **Fichier d'état.** Si `.claude/conseil/projets/<nom>.md` existe sur la branche de la session, marque-le « clos ». Ne le fusionne jamais.
5. **Réponse.** En quatre lignes au plus : ce que le conseil a retenu, les améliorations appliquées, puis exactement :

   > Projet clôturé. Tape maintenant `/clear` pour effacer la conversation, puis écris ton nouveau problème.

Ne pose aucune autre question que celle des améliorations, sauf si une étape échoue d'une façon qui ferait perdre des leçons.
