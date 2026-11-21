# volt-fpv-lab

## ECC (Everything Claude Code) installé localement

ECC v2.2.3 (github.com/affaan-m/ECC, commit 4adeee6) est installé dans ce dépôt, sans plugin, pour être chargé dans chaque session Claude Code.

Les 72 agents sont dans `.claude/agents/`, les 328 skills dans `.claude/skills/` et les 111 commandes dans `.claude/commands/` (99 commandes actuelles plus 12 anciennes commandes de compatibilité issues de `legacy-command-shims/`). Les règles communes sont dans `.claude/rules/ecc/common/` et sont chargées à chaque session.

Le runtime des hooks est dans `.claude/ecc/` (scripts, hooks, manifests, schemas, config). Ses liens symboliques `skills`, `agents`, `commands` et `rules` pointent vers les dossiers ci-dessus, si bien que `.claude/ecc` se comporte comme une racine ECC complète. Les 28 hooks sont déclarés dans `.claude/settings.json`. Leurs commandes résolvent la racine ECC en `$CLAUDE_PROJECT_DIR/.claude/ecc` au lieu de `CLAUDE_PLUGIN_ROOT`. Le fichier `.claude/ecc/hooks/hooks.json` d'origine sert de référence pour régénérer ces commandes.

Le profil de hooks est fixé par `ECC_HOOK_PROFILE` (`minimal`, `standard` ou `strict`) dans le bloc `env` de `.claude/settings.json`. `ECC_HOOKS_ENABLED=false` désactive tous les hooks, et `ECC_DISABLED_HOOKS` désactive des hooks précis par leur ID (voir `.claude/ecc/hooks/hooks.metadata.json`). La GateGuard demande de présenter des faits avant le premier Bash ou la première édition d'une session : c'est le comportement normal d'ECC.

Pour mettre ECC à jour, recloner le dépôt, recopier les mêmes dossiers, puis régénérer `.claude/settings.json` à partir du nouveau `hooks/hooks.json` en remplaçant `var e=process.env.CLAUDE_PLUGIN_ROOT;` par la résolution vers `.claude/ecc`.

## Commandes personnelles

`/board <décision>` (`.claude/commands/board.md`) convoque un conseil d'agents : un noyau fixe (Stratège, Financier, Avocat du diable) plus 1 à 3 experts invités selon le sujet, qui débattent en deux tours puis votent, avant une synthèse. Quand Théophile fait face à une décision importante et ambiguë (choix technique structurant, achat, orientation d'un projet), propose-lui de lancer `/board`, sans le lancer de toi-même car il coûte cher en tokens.
