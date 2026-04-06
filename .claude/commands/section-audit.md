# Skill : Audit d'une section entière

## Usage

```
/section-audit <chemin-section>
```

Exemple : `/section-audit physique-chimie/seconde`

### Sections disponibles

| Section | Chemin | Chapitres | Diff |
|---|---|---|---|
| Maths Seconde | `maths/seconde` | 14 | oui |
| Maths Première | `maths/premiere` | 9 | oui |
| Maths Terminale | `maths/terminale` | 11 | oui |
| Maths LGT Terminale | `maths/lgt-terminale` | 15 | non |
| Maths CAP | `maths/cap` | 7 | non |
| Maths BTS | `maths/bts` | 25 | non |
| PC Seconde | `physique-chimie/seconde` | 14 | oui |
| PC Première ICCER | `physique-chimie/premiere-iccer` | 10 | oui |
| PC Première ERA | `physique-chimie/premiere-era` | 10 | oui |
| PC Première GPT2 | `physique-chimie/premiere-gpt2` | 1 | non |
| PC Première GPT4 | `physique-chimie/premiere-gpt4` | 1 | non |
| PC Première GPT6 | `physique-chimie/premiere-gpt6` | 2 | non |
| PC Terminale ICCER | `physique-chimie/terminale-iccer` | 8 | oui |
| PC Terminale ERA | `physique-chimie/terminale-era` | 8 | oui |
| PC Terminale GPT2 | `physique-chimie/terminale-gpt2` | 2 | non |
| PC Terminale GPT4 | `physique-chimie/terminale-gpt4` | 3 | non |
| PC Terminale GPT5 | `physique-chimie/terminale-gpt5` | 5 | non |
| PC CAP | `physique-chimie/cap` | 7 | non |

---

## Objectif

Produire un **tableau de bord rapide** de tous les chapitres d'une section.

Ce skill ne lit pas chaque fichier en détail — il fait un **passage léger** sur chaque chapitre pour repérer les problèmes les plus visibles et identifier ceux qui méritent un audit approfondi (`/check-quality`, `/scientific-audit`).

---

## Instructions

### Étape 1 — Identifier la section

Depuis le chemin fourni, lister tous les sous-dossiers `chNN/` présents.
Identifier la matière (maths / physique-chimie) et le niveau (seconde, premiere-*, terminale-*, cap, bts).

### Étape 2 — Passage rapide sur chaque chapitre

Pour chaque dossier `chNN/`, effectuer les vérifications suivantes **sans lire les fichiers en entier** — utiliser Glob et des recherches ciblées :

#### 2a. Fichiers présents

Vérifier la présence de chaque fichier attendu :

| Fichier | Statut |
|---|---|
| `lecon.html` | Obligatoire |
| `exercices.html` | Obligatoire |
| `ds.html` | Obligatoire |
| `fiche.html` | Recommandé |
| `qcm.html` | Recommandé |
| `interro.html` | Recommandé |
| `activite.html` | Recommandé |
| `exercices-capacites.html` | Recommandé |
| `simulation.html` | Optionnel (info) |

#### 2b. Visuels dans les pages d'exercices

Pour `exercices.html`, `ds.html`, `interro.html` présents :
- Compter les occurrences de `<svg`, `<canvas`, `new Chart`, `<img` dans le fichier
- Compter les blocs `.exo` ou titres d'exercice
- Calculer le ratio

#### 2c. Différenciation

Pour `exercices.html` et `ds.html` :
- Vérifier la présence de `diff-socle` dans le fichier (recherche rapide)

#### 2d. Sigles interdits

Recherche rapide de `ICCER`, `ERA-MA`, `MAMA` dans le contenu de tous les fichiers du chapitre (hors balises titre et navigation).

#### 2e. Contenu vide

Rechercher les mentions "en cours de rédaction", "à compléter", "TODO" dans les fichiers.

---

### Étape 3 — Tableau de bord

Afficher un tableau synthétique, une ligne par chapitre :

```
## Audit section : physique-chimie/seconde
**14 chapitres analysés**

| Ch | Titre | Fichiers | Visuels exo | Diff | Sigles | Vide | Priorité |
|---|---|---|---|---|---|---|---|
| ch01 | Mesures et incertitudes | 8/8 ✅ | 2/8 ✅ | ✅ | ✅ | — | 🟢 |
| ch02 | Signaux et images | 5/8 ⚠ fiche, activite, exo-cap | 0/6 🔴 | ✅ | ✅ | — | 🔴 |
| ch03 | Énergie | 8/8 ✅ | 1/10 🟡 | ⚠ | ✅ | — | 🟡 |
| ch04 | ... | ... | ... | ... | ... | ... | ... |
...

**Légende :**
🔴 Critique — à traiter en priorité
🟡 Avertissement — à améliorer
🟢 OK
⚠ Problème partiel
```

#### Colonne "Fichiers"
- Format : `X/8` (nombre de fichiers obligatoires + recommandés présents sur 8)
- Indiquer lequel manque si < 8
- `simulation.html` (optionnel) n'est pas compté dans le total mais signalé si présent

#### Colonne "Visuels exo"
- Format : `nb_visuels/nb_exercices`
- 🔴 si nb_visuels == 0
- 🟡 si ratio < 0,25 (PC) ou < 0,20 (maths géométrie/fonctions)
- ✅ sinon

#### Colonne "Diff"
- ✅ si `diff-socle` trouvé dans exercices.html et ds.html
- ⚠ si trouvé dans un seul des deux
- 🔴 si absent des deux

#### Colonne "Sigles"
- ✅ si aucun sigle interdit détecté
- 🔴 + nombre d'occurrences si trouvé

#### Colonne "Vide"
- — si aucun fichier vide
- ⚠ + nom du fichier si contenu vide détecté

#### Colonne "Priorité"
- 🔴 si au moins un point CRITIQUE (0 visuel, fichier obligatoire manquant, sigle interdit, contenu vide)
- 🟡 si au moins un AVERTISSEMENT
- 🟢 si tout est OK

---

### Étape 4 — Résumé et recommandations

Après le tableau, afficher :

```
### Résumé
- X chapitres à traiter en priorité 🔴
- X chapitres avec avertissements 🟡
- X chapitres OK 🟢

### Chapitres prioritaires — actions recommandées
1. ch02 — 0 visuel dans exercices.html → /check-quality physique-chimie/seconde/ch02
2. ch05 — ds.html manquant → /generate-ds ou créer manuellement
3. ch09 — sigle interdit détecté (2 occurrences) → /check-sigles physique-chimie/seconde/ch09

### Prochaine étape
Pour un audit détaillé d'un chapitre spécifique :
→ /check-quality <chemin-chapitre>
→ /scientific-audit <chemin-chapitre>/lecon.html
```

---

## Étape 5 — Mettre à jour le journal des audits

Après avoir affiché le rapport, mettre à jour `audits/audit-log.md` :

1. Pour chaque chapitre analysé, chercher s'il a déjà une ligne dans le tableau
2. Si oui : mettre à jour la colonne `/section-audit` avec la date du jour (format `YYYY-MM-DD`) et le résultat (🔴 / 🟡 / 🟢)
3. Si non : ajouter une nouvelle ligne pour chaque chapitre
4. Mettre à jour la date `Dernière mise à jour` en haut du fichier

---

## Règles

- Ne PAS modifier les fichiers — seulement analyser et rapporter
- Rester rapide : ne pas lire les fichiers ligne par ligne — faire des recherches ciblées
- Si la section contient plus de 15 chapitres, traiter par groupes de 8 et afficher les tableaux au fur et à mesure
- Toujours terminer par les recommandations d'actions prioritaires
