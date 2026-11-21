# volt-fpv-lab

## ECC (Everything Claude Code) installé localement

ECC v2.2.3 (github.com/affaan-m/ECC, commit 4adeee6) est installé dans ce dépôt, sans plugin, pour être chargé dans chaque session Claude Code.

Les 72 agents sont dans `.claude/agents/`, les 328 skills dans `.claude/skills/` et les 111 commandes dans `.claude/commands/` (99 commandes actuelles plus 12 anciennes commandes de compatibilité issues de `legacy-command-shims/`). Les règles communes sont dans `.claude/rules/ecc/common/` et sont chargées à chaque session.

Le runtime des hooks est dans `.claude/ecc/` (scripts, hooks, manifests, schemas, config). Ses liens symboliques `skills`, `agents`, `commands` et `rules` pointent vers les dossiers ci-dessus, si bien que `.claude/ecc` se comporte comme une racine ECC complète. Les 28 hooks sont déclarés dans `.claude/settings.json`. Leurs commandes résolvent la racine ECC en `$CLAUDE_PROJECT_DIR/.claude/ecc` au lieu de `CLAUDE_PLUGIN_ROOT`. Le fichier `.claude/ecc/hooks/hooks.json` d'origine sert de référence pour régénérer ces commandes.

Le profil de hooks est fixé par `ECC_HOOK_PROFILE` (`minimal`, `standard` ou `strict`) dans le bloc `env` de `.claude/settings.json`. `ECC_HOOKS_ENABLED=false` désactive tous les hooks, et `ECC_DISABLED_HOOKS` désactive des hooks précis par leur ID (voir `.claude/ecc/hooks/hooks.metadata.json`). La GateGuard demande de présenter des faits avant le premier Bash ou la première édition d'une session : c'est le comportement normal d'ECC.

Pour mettre ECC à jour, recloner le dépôt, recopier les mêmes dossiers, puis régénérer `.claude/settings.json` à partir du nouveau `hooks/hooks.json` en remplaçant `var e=process.env.CLAUDE_PLUGIN_ROOT;` par la résolution vers `.claude/ecc`.

## Commandes personnelles

`/board <sujet>` (`.claude/commands/board.md`) réunit l'entreprise d'agents de Théophile, organisée comme une start-up. Le Directeur général (Claude, qui ne vote pas) dirige un comité de direction fixe (Stratège, Financier, Avocat du diable), des pôles convoqués selon le sujet (chacun avec un responsable) et des spécialistes sur modèle léger, recrutés sans limite. Une séance enchaîne un tour à l'aveugle, des face-à-face, une contre-expertise, un vote, un atelier si un livrable est demandé, puis une synthèse. Il existe trois formats : `flash`, `standard` et `complet`. Les agents sont continués avec SendMessage plutôt que relancés. Le conseil peut consulter Théophile en cas d'impasse. Un tableau en direct s'ouvre à droite, à partir du gabarit `.claude/board/board.html` (seul son bloc JSON est modifié). L'expérience de l'équipe (des leçons de méthode générales, jamais le contenu d'un projet) est dans `.claude/board/memoire/retex.md`. À la fin de chaque séance, elle est enrichie et fusionnée automatiquement dans la branche par défaut, sans rien demander à Théophile. Le contenu d'un projet reste dans sa session et n'est jamais fusionné : pour reprendre un projet, Théophile revient dans la même session. Si la décision mène à un achat, la séance se termine par une liste de pièces avec des liens vérifiés. Quand Théophile fait face à une décision importante et ambiguë (choix technique structurant, achat, orientation d'un projet), propose-lui de lancer `/board`, sans le lancer de toi-même car il coûte cher en tokens.
