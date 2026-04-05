# Maths & Sciences LP — Site pédagogique

Espace pédagogique complet pour les classes de **Bac Professionnel**, **CAP**, **BTS** et **Terminale LGT** en mathématiques et physique-chimie.

🌐 **Site en ligne :** [maths-sciences-lp.github.io](https://maths-sciences-lp.github.io)

---

## Niveaux couverts

| Niveau | Maths | Physique-Chimie |
|---|---|---|
| Seconde Bac Pro (MAMA) | 14 chapitres | 14 chapitres |
| Première Bac Pro (ICCER, ERA-MA, Gpts 2/4/6) | 9 chapitres | 10 chapitres × 6 groupements |
| Terminale Bac Pro (ICCER, ERA-MA, Gpts 2/4/5) | 16 chapitres | 8 chapitres × 5 groupements |
| CAP (groupement 1 : MIT, Ébéniste, SDG) | 7 chapitres | 7 chapitres |
| BTS (toutes spécialités) | 25 chapitres | — |
| Terminale LGT (voie générale/technologique) | 15 chapitres | — |

---

## Contenus disponibles

Chaque chapitre peut contenir jusqu'à 8 types de pages :

| Type | Description | Nombre |
|---|---|---|
| `lecon.html` | Cours complet (identique pour tous les élèves) | **152** |
| `exercices.html` | Exercices différenciés (Socle / Standard / Approfondissement) | **130** |
| `ds.html` | Devoir surveillé différencié | **116** |
| `fiche.html` | Fiche de révision / mémo | **112** |
| `qcm.html` | QCM interactif avec score et correction automatique | **98** |
| `interro.html` | Interrogation courte (10-15 min, barème /20) | — |
| `exercices-capacites.html` | Exercices organisés par capacités du programme | — |
| `activite.html` | Activité de découverte (situation-problème guidée) | — |

**Total : 608+ pages de contenu pédagogique**

---

## Simulations interactives

**70 simulations** dans le dossier `simulations/`, couvrant :
- Fonctions et graphiques (tracé dynamique, variations)
- Géométrie (trigonométrie, vecteurs, transformations)
- Statistiques et probabilités
- Physique (circuits électriques, thermique, mécanique)
- Chimie (modèles moléculaires, réactions)

Chaque simulation est ancrée dans un chapitre et un programme officiel.

---

## Automatismes

**22 pages** d'entraînement rapide dans `automatismes/` :
calcul mental, réflexes de calcul, manipulations algébriques — organisées par niveau et thème.

---

## Différenciation pédagogique

Les exercices et devoirs sont différenciés en **3 niveaux** :

- 🟢 **Socle** — exercices très guidés, étape par étape, pour les élèves en difficulté
- 🔵 **Standard** — exercices du programme, contextes professionnels variés
- 🟣 **Approfondissement** — problèmes ouverts, mise en équation autonome, niveau BTS

Le toggle de différenciation (`diff.js`) mémorise le choix de l'élève entre les pages.

---

## Contextes professionnels

Les exercices utilisent des contextes issus des filières réelles du lycée :

| Filière | Métiers |
|---|---|
| ICCER | Plombier chauffagiste, installateur thermique, technicien CVC |
| ERA / MA | Menuisier, menuisier agenceur, ébéniste, technicien d'agencement |
| MAMA (Seconde) | Menuisier, métreur, artisan menuisier |
| CAP MIT | Installateur thermique, technicien de maintenance |
| CAP Ébéniste | Ébéniste, fabricant de meubles |

---

## Structure du dépôt

```
/
├── styles.css              ← Feuille de style partagée
├── print.css               ← Styles d'impression (A4)
├── nav.js                  ← Navigation auto-générée
├── diff.js                 ← Toggle différenciation pédagogique
├── qcm.js                  ← Fonctions QCM interactifs
├── comp.js                 ← Filtrage par capacité
├── maths/
│   ├── seconde/ch01..ch14/
│   ├── premiere/ch01..ch09/
│   ├── terminale/ch01..ch16/
│   ├── lgt-terminale/ch01..ch15/
│   ├── cap/ch01..ch07/
│   └── bts/ch01..ch25/
├── physique-chimie/
│   ├── seconde/ch01..ch14/
│   ├── premiere-iccer/ch01..ch10/
│   ├── premiere-era/ch01..ch10/
│   ├── premiere-gpt2/4/6/
│   ├── terminale-iccer/ch01..ch08/
│   ├── terminale-era/ch01..ch08/
│   ├── terminale-gpt2/4/5/
│   └── cap/ch01..ch07/
├── simulations/            ← 70 simulations interactives
├── automatismes/           ← 22 pages d'automatismes
├── co-intervention/        ← Séances co-intervention maths/sciences
├── prompts/                ← Prompts pédagogiques de référence
├── audits/                 ← Audits qualité et feuille de route
├── scripts/                ← Outils de maintenance Python/Node
└── pdf/                    ← Programmes officiels Bac Pro & BTS
```

---

## Technologies utilisées

- **HTML/CSS/JS** pur — aucun framework, aucune dépendance serveur
- **MathJax 3** — rendu des formules mathématiques (LaTeX)
- **Chart.js** — graphiques interactifs
- **SVG / Canvas** — figures géométriques et simulations
- **GitHub Pages** — hébergement statique

---

## Licence

Contenu pédagogique libre d'utilisation pour un usage éducatif non commercial.
