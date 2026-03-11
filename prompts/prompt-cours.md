# Prompt de référence — Génération de pages de cours

## Rôle
Ce fichier définit les règles à appliquer pour générer les pages de cours du site pédagogique du lycée professionnel.

---

## Niveau cible
**Bac Professionnel** (Seconde, Première, Terminale)

---

## Structure obligatoire d'une page de cours

Une page de cours doit comporter les sections suivantes dans cet ordre :

1. **Titre du cours** — clair et explicite, en lien avec le programme
2. **Objectifs pédagogiques** — liste des compétences visées (3 à 5 points)
3. **Introduction / Mise en situation** — contexte professionnel concret, ancré dans la filière
4. **Contenu du cours** — découpé en parties numérotées avec titres
5. **Points clés à retenir** — résumé synthétique en fin de cours
6. **Vers les exercices** — lien ou invitation à pratiquer

---

## Contraintes de contenu

- Langage **clair et accessible**, adapté au niveau Bac Pro
- Éviter le jargon mathématique non défini
- Chaque notion nouvelle doit être **définie avant d'être utilisée**
- Exemples **concrets et contextualisés** selon la filière (voir prompts de filière)
- Formules mathématiques présentées avec explication de chaque variable
- Progression logique : du simple vers le complexe

---

## Contraintes techniques HTML

- Structure HTML valide et sémantique (`<section>`, `<article>`, `<h1>` à `<h3>`, etc.)
- Utilisation des classes CSS existantes du site
- Formules mathématiques rendues avec **MathJax** ou **KaTeX**
- Tableaux structurés avec `<thead>` et `<tbody>`
- Accessibilité : attributs `alt` sur les images, contrastes respectés

---

## Graphiques et animations

- Inclure des graphiques ou animations **si cela aide la compréhension**
- Utiliser **Chart.js** ou **Desmos** pour les représentations graphiques
- Animations légères en CSS ou JavaScript pour illustrer des variations
- Chaque graphique doit comporter : titre, légendes des axes, unités

---

## Cohérence pédagogique

- Le cours doit s'inscrire dans la **progression annuelle** du lycée
- Les exemples doivent être tirés des **situations professionnelles** de la filière concernée
- Ne pas introduire de contenu hors programme sans le signaler explicitement

---

## Références à combiner

Avant de générer un cours, lire aussi :
- `prompt-exercices.md` pour anticiper les exercices associés
- Le prompt de filière correspondant (`prompt-filiere-ticcer.md`, `prompt-filiere-era-ma.md` ou `prompt-filiere-2mama.md`)
