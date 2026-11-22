# Protocole des outils

Tout le conseil peut améliorer ses outils en cours de mission : trouver, installer, créer, activer ou désactiver des skills. En général, c'est le Responsable des outils (fiche `annuaire/outilleur.md`) qui s'en charge, recruté par le Président ou par un conseiller.

## Ce que l'équipe peut faire seule

1. **Chercher.** Regarde d'abord le catalogue (`catalogue.md`) et les 328 skills de `.claude/skills/`, puis lance `skill-scout`. Les dépôts publics se clonent en lecture (`git clone --depth 1`) dans le scratchpad, jamais dans le dépôt.
2. **Contrôler avant d'installer.** Lis **tous** les fichiers du skill, pas seulement `SKILL.md`. Refuse tout skill qui :
   - lance des commandes réseau vers des hôtes inconnus, ou envoie des données dehors ;
   - demande des secrets, des jetons ou des identifiants ;
   - ajoute des hooks, modifie `.claude/settings.json` ou les permissions ;
   - exécute du code obscurci, téléchargé à la volée ou installé avec des droits root ;
   - contredit les règles du dépôt ou les fiches du conseil.
   Préfère les sources sérieuses : `anthropics/skills`, ECC, des auteurs connus, une licence claire et une activité récente.
3. **Installer.** Copie le dossier du skill dans `.claude/skills/<nom>/`, ajoute en tête de son `SKILL.md` une ligne de provenance (`<!-- source : <dépôt>@<commit>, licence <x>, vérifié par <id> le <date> -->`), commite et pousse sur la branche de ta session.
4. **Utiliser tout de suite.** Un skill installé en cours de session n'apparaît pas toujours dans la liste avant la session suivante. Pour l'utiliser immédiatement, lis son `SKILL.md` avec l'outil Read et applique-le, ou donne son chemin dans le prompt du sous-agent qui en a besoin.
5. **Créer.** Si rien n'existe, crée le skill avec `anthropic-skills:skill-creator` dans `.claude/skills/<nom>/`. Écris-le en règles générales, sans contenu de projet.
6. **Désactiver.** Un skill inutile, redondant ou qui dégrade le rendu se déplace dans `.claude/skills-off/<nom>/` (avec `git mv`). Pour le réactiver, on le remet dans `.claude/skills/`. Ne supprime jamais un skill : désactive-le.
7. **Bibliothèques.** Les paquets Python ou Node nécessaires à une mission (par exemple `cadquery` pour la 3D ou `moviepy` pour la vidéo) s'installent dans la session avec `pip` ou `npm`, sans les ajouter au dépôt.

## Ce qui demande l'accord de Théophile

Le Président le consulte (étape « Consulter Théophile ») avant :

- d'installer un **plugin** ou un **serveur MCP**, ou de connecter un **connecteur** (Gmail, Canva, Drive…) ;
- d'ajouter ou de modifier un **hook** ou une **permission** ;
- d'ajouter un **hôte réseau** à l'environnement, ou d'enregistrer une **clé d'API**.

Ces changements touchent à la sécurité ou à des comptes : l'équipe les propose, Théophile décide.

## Garder ce qui marche

Rends compte de chaque outil installé, créé ou désactivé dans ton rapport : nom, source, raison et effet sur le rendu. Le Head of Common Sense vérifie qu'un outil installé a bien servi le livrable. À la clôture, le Président publie dans la branche par défaut, avec le retex et l'annuaire, les skills qui ont fait leurs preuves et les désactivations justifiées. Un skill qui n'a pas servi reste sur la branche de la session.
