---
description: Clôture le projet en cours du conseil pour repartir de zéro en gardant l'organisation. Enregistre les leçons, archive les conseillers du projet, remet une équipe vierge en veille, puis rappelle de taper /clear.
argument-hint: "(aucun argument)"
---

# /fin : clôturer le projet

Théophile a décidé de clôturer le projet en cours. Tu es le Président (`.claude/commands/president.md`).

1. **Clôture.** Applique l'étape « 8. Clôture » de `.claude/commands/president.md` : leçons générales des conseillers et du Head of Common Sense, section « Leçons » des fiches, `retex.md`, nouvelles fiches et skills qui ont fait leurs preuves, publiés dans la branche par défaut. Si aucun projet n'est en cours dans cette conversation, saute cette étape et dis-le en une phrase.
2. **Archiver l'équipe du projet.** Appelle `list_sessions` avec `children: true` et archive avec `archive_session` toutes les sessions enfants qui ont servi au projet. Une session archivée ne reçoit plus rien et ne sera jamais réutilisée : son contenu ne peut pas fuiter vers le projet suivant.
3. **Remettre une équipe vierge en veille.** Recrée sans `prompt` les sessions de base décrites dans « Équipe en veille » de `president.md`, avec `source_url` du dépôt et la branche par défaut en `source_revision`. Elles restent rangées sous cette session dans la barre latérale et ne consomment rien tant qu'elles n'ont pas de mission.
4. **Tableau.** Passe le tableau du projet à `phase: "terminé"`, avec un `statut` et un `point.etat` qui disent que le projet est clos, puis republie-le : il reste consultable dans les artefacts. Le prochain projet ouvrira un tableau vierge.
5. **Fichier d'état.** Si `.claude/conseil/projets/<nom>.md` existe sur la branche de la session, marque-le « clos ». Ne le fusionne jamais.
6. **Réponse.** En trois lignes au plus : ce que le conseil a retenu, les sessions archivées et recréées, puis exactement :

   > Projet clôturé. Tape maintenant `/clear` pour effacer la conversation, puis écris ton nouveau problème.

Ne pose aucune question, sauf si une étape échoue d'une façon qui ferait perdre des leçons.
