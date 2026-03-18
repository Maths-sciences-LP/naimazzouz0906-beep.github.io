# Audit Doublons de pages

**Date** : 2026-03-18
**Derniere mise a jour** : 2026-03-18 (corrections appliquees)
**Perimetre** : Pages en doublon ou hors schema standard (automatismes, QCM, interrogations)

---

## Resume executif

Deux pages servent de point d'entree aux automatismes mathematiques :
- `/automatismes.html` (racine, 46 Ko, 738 lignes)
- `/automatismes/index.html` (23 Ko, 518 lignes)

Ces pages couvrent les memes themes (Seconde, Premiere, Terminale) mais avec des approches differentes. Les liens depuis le reste du site sont **incoherents** : certaines pages pointent vers l'une, d'autres vers l'autre, et deux pages pointent vers les deux.

---

## Problemes identifies

### 1. Doublon fonctionnel entre les deux pages (gravite : HAUTE)

| Dimension | `automatismes.html` (racine) | `automatismes/index.html` |
|---|---|---|
| **Role** | Mega-page avec exercices flash inline | Hub moderne avec cards vers 22 pages thematiques |
| **Taille** | 46 Ko, 738 lignes | 23 Ko, 518 lignes |
| **Design** | Ancien (tabs basiques, inline styles + styles.css) | Moderne (cards, gradients, hover, 100% inline) |
| **Exercices** | Inline avec corrections cachees (bouton voir/cacher) | Deportes dans 22 pages thematiques individuelles |
| **Impression** | Optimise (print.css + @media print) | Pas d'optimisation print |
| **MathJax** | tex-mml-chtml.js | tex-svg.js |
| **Navigation** | Tabs Seconde/Premiere/Terminale | Tabs + grid de cards cliquables |
| **Lien nav.js** | Oui | Non (page autonome) |

**Contenu de `automatismes.html` (racine) :**
- 6 domaines Seconde avec exercices flash complets et corrections
- 7 domaines Premiere avec exercices flash complets et corrections
- 8 domaines Terminale avec exercices flash complets et corrections
- Explication pedagogique detaillee (principe de cumul)
- Aucun lien vers les pages thematiques individuelles

**Contenu de `automatismes/index.html` :**
- 6 cards Seconde → liens vers pages thematiques
- 7 cards Premiere → liens vers pages thematiques
- 8 cards Terminale → liens vers pages thematiques
- Section "Pourquoi les automatismes ?"
- Guide d'utilisation en 4 etapes
- Aucun exercice inline

### 2. Liens incoherents depuis le site (gravite : CRITIQUE)

| Page source | Lien | Cible |
|---|---|---|
| `index.html` (accueil) | `automatismes.html` | Racine |
| `maths-2nde-mama.html` | `automatismes.html` | Racine |
| `maths-1ere-pro.html` | `automatismes.html` | Racine |
| `maths-term-erama.html` | `automatismes.html` (Seconde) | Racine |
| `maths-term-erama.html` | `automatismes/index.html` (Terminale) | Dossier |
| `maths-term-iccer.html` | `automatismes.html` (Seconde) | Racine |
| `maths-term-iccer.html` | `automatismes/index.html` (Terminale) | Dossier |

**Resultat :** les eleves de Terminale arrivent sur une page differente selon le lien clique. Deux experiences utilisateur contradictoires pour le meme contenu.

### 3. Les 22 pages thematiques ne sont accessibles que via `automatismes/index.html` (gravite : MOYENNE)

Pages thematiques existantes dans `/automatismes/` :

**Seconde (6) :**
- seconde-calcul-numerique.html
- seconde-calcul-litteral.html
- seconde-proportionnalite.html
- seconde-grandeurs.html
- seconde-geometrie.html
- seconde-statistiques.html

**Premiere (7) :**
- premiere-stats-probas.html
- premiere-algebre.html
- premiere-fonctions.html
- premiere-geometrie.html
- premiere-calculs-commerciaux.html
- premiere-suites.html
- premiere-derivation.html

**Terminale (8) :**
- probabilites.html
- suites.html
- polynomes.html
- derivation.html
- vecteurs.html
- terminale-exp-log.html
- terminale-trigonometrie.html
- terminale-integration.html

**Aucune** de ces pages n'est liee depuis `automatismes.html` (racine). Les eleves qui arrivent sur la page racine n'ont jamais acces a ces 22 pages detaillees.

### 4. CSS non conforme dans `automatismes.html` (gravite : BASSE)

La page racine contient environ 200 lignes de CSS inline qui definissent des classes specifiques (`.level-tab`, `.auto-domain`, `.flash-series`, `.flash-corr`, etc.) non presentes dans `styles.css`. Certaines de ces classes pourraient etre utiles si elles etaient centralisees.

### 5. `physique-chimie/seconde/ch07/qcm.html` — page orpheline (gravite : HAUTE)

Page QCM interactive sur "Structure de la matiere" (15 questions, auto-correction JS).

| Dimension | Detail |
|---|---|
| **Format** | QCM interactif avec feedback instantane et score |
| **Contenu** | 15 questions : atomes, Z, neutrons, couches electroniques, ions, molecules, etats |
| **Duree** | 15-20 min, sans calculatrice |
| **Doublon avec `exercices.html` ?** | **Non** — format different (QCM interactif vs exercices rediges) |
| **Liee depuis le sommaire ?** | **Non** — page orpheline, introuvable par navigation |
| **CSS** | 25 classes inline (`.qcm-header`, `.q-block`, `.options`, `.q-feedback`, `.score-box`, etc.) |
| **nav.js** | Oui |
| **print.css** | Oui |

**Probleme :** la page existe mais aucun lien ne permet d'y acceder. Le sommaire `pc-2nde-pro.html` ne liste que lecon.html, exercices.html, ds.html pour le ch07.

**Actions possibles :**
- A. Ajouter un lien vers qcm.html dans le sommaire du ch07 (conserver la page)
- B. Fusionner le contenu QCM dans exercices.html (supprimer la page)
- C. Centraliser les classes CSS QCM dans styles.css si d'autres QCM sont prevus

### 6. `maths/terminale/ch04/interro.html` — doublon avec `ds.html` (gravite : HAUTE)

Interrogation ecrite sur "Polynomes de degre 3" (40 min, 20 pts, differenciation socle/standard/appro).

| Dimension | `interro.html` | `ds.html` |
|---|---|---|
| **Titre** | Interrogation ecrite (40 min) | Devoir Surveille (1h) |
| **Format** | Differencie socle/standard/appro | Differencie socle/standard/appro |
| **Bareme** | 20 points (4 exos par niveau) | 20 points (4 exos par niveau) |
| **Contenu** | Reconnaissance, coefficients, images, derivees | Reconnaissance, coefficients, images, derivees |
| **Chevauchement** | ~85% identique a ds.html | ~85% identique a interro.html |
| **Corrections** | Oui (bouton "Voir la correction") | Oui (bouton "Voir la correction") |
| **Liee ?** | Oui — depuis `maths-term-iccer.html` et `maths-term-erama.html` | Oui — depuis les memes sommaires |
| **print.css** | Non | Oui |
| **diff.js** | Oui | Oui |

**Probleme :** les deux pages evaluent exactement les memes competences avec la meme structure differenciation. La seule difference est la duree (40 min vs 1h) et quelques variations mineures de formulation. Un eleve qui fait les deux n'apprend rien de nouveau.

**Actions possibles :**
- A. Supprimer interro.html et ne garder que ds.html (recommande — evite la maintenance double)
- B. Differencier reellement le contenu : interro = evaluation rapide/diagnostique, ds = evaluation sommative complete
- C. Fusionner les exercices uniques de interro.html dans ds.html avant suppression

---

## Analyse et recommandation

### Option A : Conserver `automatismes/index.html` comme page unique (RECOMMANDE)

**Avantages :**
- Architecture modulaire (hub + 22 pages individuelles)
- Design moderne et maintenable
- Ajout de contenu = un fichier, pas une mega-page a modifier
- Meilleur SEO (une page par theme)
- Coherent avec l'architecture du reste du site

**Actions :**
1. Mettre a jour tous les liens vers `automatismes/index.html`
2. Migrer le contenu "exercices flash" de la page racine vers les pages thematiques si absent
3. Supprimer ou archiver `automatismes.html` (racine)

### Option B : Fusionner les deux (exercices flash dans le hub)

**Avantages :**
- Conserve l'acces immediat aux exercices flash
- Un seul point d'entree

**Inconvenients :**
- Page plus lourde
- Doublon avec les pages thematiques

### Option C : Garder les deux avec roles distincts

- `automatismes.html` → "Edition enseignant" (impression)
- `automatismes/index.html` → "Edition eleve" (navigation)

**Inconvenient :** maintenance double, confusion de liens

---

## Corrections realisees

- **2026-03-18** : Option A retenue — `automatismes/index.html` conserve comme page unique
- **2026-03-18** : Liens mis a jour dans 5 fichiers (`index.html`, `maths-2nde-mama.html`, `maths-1ere-pro.html`, `maths-term-erama.html`, `maths-term-iccer.html`) pour pointer vers `automatismes/index.html`
- **2026-03-18** : Fusion des 2 liens distincts (Automatismes 2nde + Automatismes Terminale) en un seul dans `maths-term-erama.html` et `maths-term-iccer.html`
- **2026-03-18** : Verification du contenu — les 22 pages thematiques sont plus completes que la page racine (QCM, 3 niveaux, feedbacks vs simples reponses flash). Aucune migration necessaire.
- **2026-03-18** : Suppression de `automatismes.html` (racine) — doublon elimine

---

## Ameliorations restantes

### Priorite critique
- [x] Unifier les liens : toutes les pages du site doivent pointer vers la meme page d'automatismes
- [x] Corriger `maths-term-erama.html` et `maths-term-iccer.html` qui pointent vers les deux pages

### Priorite haute
- [x] Choisir la page a conserver (recommandation : `automatismes/index.html`)
- [x] Verifier que les 22 pages thematiques contiennent bien les exercices flash (sinon migrer depuis la racine)
- [x] Supprimer ou archiver la page non retenue

### Priorite haute (nouvelles pages)
- [ ] `physique-chimie/seconde/ch07/qcm.html` : ajouter un lien dans le sommaire OU fusionner dans exercices.html (page orpheline)
- [ ] `maths/terminale/ch04/interro.html` : supprimer OU differencier reellement de ds.html (~85% doublon)
- [ ] Centraliser les 25 classes CSS inline de qcm.html dans `styles.css` si d'autres QCM sont prevus

### Priorite moyenne
- [ ] Ajouter l'optimisation impression aux pages thematiques automatismes si necessaire
- [ ] Centraliser les classes CSS utiles (`.flash-series`, etc.) dans `styles.css` si reutilisees

### Priorite basse
- [ ] Harmoniser le rendu MathJax (tex-mml-chtml vs tex-svg) sur toutes les pages automatismes
