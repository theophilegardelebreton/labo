# Catalogue de recrutement

Le Président, les conseillers et le Recruteur piochent ici pour composer une équipe en quelques secondes, quel que soit le problème. Il y a trois sources, à combiner librement.

1. **Les fiches maison** (`annuaire/`), recrutées comme sous-agents (`general-purpose`) avec le contenu de la fiche en tête du prompt.
2. **Les 40 agents ECC actifs** (`.claude/agents/`), appelés par `subagent_type`. Ils sont surtout orientés logiciel. 32 agents hors sujet (langages inutilisés, réseau, santé, HarmonyOS) sont rangés dans `.claude/agents-off/` ; on en réactive un en le remettant dans `.claude/agents/`.
3. **Les rôles sur mesure** : un sous-agent `general-purpose` avec un nom de métier, un regard en une ligne et, si besoin, les **skills** du dépôt à charger (`.claude/skills/`, 211 actifs, les autres rangés dans `.claude/skills-off/`). C'est la source principale hors logiciel : styliste, ingénieur textile, juriste, architecte, nutritionniste, acheteur, monteur vidéo… Tout métier peut être créé.

Avant d'appeler un agent ECC, lis la `description` dans l'en-tête de son fichier pour vérifier qu'il convient.

## Fiches maison

| Fiche | Rôle | Quand |
| --- | --- | --- |
| `recruteur.md` | compose l'équipe d'un conseiller | équipe de plus de deux personnes, ou spécialiste à trouver |
| `money-maker.md` | maximise les gains à court terme : offre, prix, marge, premiers clients | business, vente, produit commercialisé |
| `outilleur.md` | trouve, vérifie, installe, crée ou désactive les skills dont l'équipe a besoin | rendu à améliorer, travail répété, outil absent |
| `visionnaire.md` | Stratège prospectif : scénarios à 1, 3 et 10 ans, potentiel maximal | business, projet à fort potentiel, choix qui engage des années |
| `avocat-du-diable.md` | contredit tout, par principe | permanent (sous-agent à part), mais un conseiller peut aussi en recruter un dans son équipe pour un débat interne |

## Agents ECC par domaine

| Domaine | Agents |
| --- | --- |
| Conception et planification | `planner`, `architect`, `code-architect`, `code-explorer`, `spec-miner`, `gan-planner` |
| Développement et tests | `tdd-guide`, `gan-generator`, `gan-evaluator`, `e2e-runner`, `pr-test-analyzer`, `performance-optimizer`, `refactor-cleaner`, `code-simplifier` |
| Revue et qualité | `code-reviewer`, `silent-failure-hunter`, `type-design-analyzer`, `comment-analyzer`, `commit-reviewer`, `agent-evaluator` |
| Sécurité | `security-reviewer`, `opensource-sanitizer` |
| Revue par langage | `python-reviewer`, `typescript-reviewer`, `react-reviewer` |
| Réparation de build | `build-error-resolver`, `react-build-resolver` |
| Données, IA et ML | `database-reviewer`, `rag-pipeline-reviewer` |
| Documentation | `doc-updater`, `docs-lookup` |
| Marketing et web | `marketing-agent`, `seo-specialist`, `a11y-architect` |
| Open source | `opensource-forker`, `opensource-packager` |
| Organisation et agents | `chief-of-staff`, `loop-operator`, `harness-optimizer`, `conversation-analyzer` |

## Skills utiles hors logiciel

| Domaine | Skills |
| --- | --- |
| Business et argent | `market-research`, `competitive-platform-analysis`, `benchmark-methodology`, `competitive-report-structure`, `investor-materials`, `investor-outreach`, `lead-intelligence`, `finance-billing-ops`, `customer-billing-ops`, `master-agreement-generator`, `product-lens` |
| Marque et contenus | `brand-discovery`, `brand-voice`, `article-writing`, `content-engine`, `marketing-campaign`, `seo`, `social-publisher`, `crosspost`, `short-video-distribution` |
| Vidéo et visuel | `video-editing`, `remotion-video-creation`, `manim-video`, `fal-ai-media`, `frontend-slides`, `design-system`, `frontend-design-direction`, `taste` |
| Fabrication et logistique | `production-scheduling`, `quality-nonconformance`, `inventory-demand-planning`, `customs-trade-compliance`, `returns-reverse-logistics` |
| Recherche et faits | `deep-research`, `scientific-thinking-literature-review`, `scientific-db-uspto-database` (brevets), `osint-investigation`, `data-scraper-agent`, `dashboard-builder` |
| Décision | `council`, `santa-method` |

## Combinaisons types

Ce sont des points de départ, pas des recettes : le Conseiller des opérations et le Recruteur adaptent.

| Problème | Conseillers | Recrues typiques |
| --- | --- | --- |
| Lancer un business | Stratégie, Création, Opérations | Money Maker, Stratège prospectif, `marketing-agent`, analyste marché (`market-research`), juriste sur mesure |
| Créer un vêtement (un slip, par exemple) | Création, Technique, Stratégie | styliste, ingénieur textile, modéliste patronage, acheteur tissus, Money Maker si c'est pour vendre |
| Concevoir un objet technique | Technique, Stratégie | ingénieur mécanique, électronicien, modélisateur 3D, acheteur sourceur, spécialiste des normes |
| Une application ou un site | Technique, Création | `planner`, `tdd-guide`, `code-reviewer`, `security-reviewer`, `e2e-runner`, designer UX |
| Une vidéo | Création | scénariste, monteur (`video-editing`), motion designer (`remotion-video-creation`), `seo-specialist` |
| Réviser un examen | Technique (scientifique) | professeur sur mesure de la matière, correcteur, générateur d'exercices |
