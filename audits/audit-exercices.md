# Audit Exercices et DS

**Date** : 2026-03-16
**Dernière mise à jour** : 2026-03-16
**Périmètre** : pages exercices.html et ds.html — corrections, qualité, complétude

---

## Problemes identifies

### 1. Corrections potentiellement incomplètes

Un sondage sur les pages d'exercices montre un déséquilibre entre exercices et corrections :

| Page | Blocs `.exo` | Blocs `.corr` | Écart |
|---|---|---|---|
| `maths/seconde/ch01/exercices.html` | 39 | 12 | **-27** |
| `maths/premiere/ch01/exercices.html` | 36 | 24 | **-12** |

Cela suggère que de nombreux exercices n'ont pas de correction associée. Un audit complet de toutes les pages d'exercices est nécessaire pour quantifier le problème.

### 2. Absence de différenciation en maths/premiere

_(Détaillé dans audit-pedagogique.md)_

Les 9 pages exercices.html et 9 pages ds.html de `maths/premiere` n'ont pas de niveaux de difficulté (socle/standard/appro). Tous les exercices sont indifférenciés.

### 3. 29 pages BTS stub (contenu placeholder)

**Gravité : MOYENNE**

Dans `maths/bts/`, 29 fichiers (exercices.html et ds.html) ne contiennent qu'un message placeholder : *"Ce devoir surveillé est en cours de rédaction. Le contenu sera disponible prochainement."*

Chapitres concernés : ch01 (ds), ch02 (ds), ch03 (ds + exo), ch04 (ds), ch05 (ds), ch06 (ds + exo), ch07 (ds + exo), ch08 (ds), ch09 (ds + exo), ch10 (ds + exo), ch11 (ds + exo), ch12 (ds), ch13 (ds), ch14 (ds + exo), ch15 (ds + exo), ch16 (ds + exo), ch17 (ds + exo), ch18 (ds + exo).

### 4. Deux mécanismes de correction coexistent

Les corrections utilisent deux patterns différents selon les sections :
- **maths/premiere** : `<details class="corr-wrap"><summary class="corr-btn">` (HTML5 sémantique, sans JS)
- **physique-chimie** : boutons `.bc` avec `onclick` (nécessite JS)

Les deux fonctionnent, mais l'incohérence peut créer de la confusion lors de la maintenance.

### 5. Boutons "Voir la correction" (.bc)

À vérifier : chaque bloc `.corr` doit être précédé d'un bouton `.bc` pour que l'élève puisse afficher la correction. Des corrections sans bouton resteraient invisibles.

### 4. Qualité des DS

Points à auditer systématiquement :
- Les DS sont-ils calibrés en durée (1h, 2h) ?
- Comportent-ils un barème visible ?
- Respectent-ils la progression des chapitres précédents ?
- Contiennent-ils les 3 niveaux de différenciation (premiere/terminale) ?

---

## Corrections realisees

- Aucune à ce stade.

---

## Ameliorations restantes

### Priorité haute
- [ ] Réaliser un inventaire complet : nombre de `.exo` vs `.corr` sur chaque page d'exercices
- [ ] Ajouter les corrections manquantes (estimé : plusieurs dizaines d'exercices)
- [ ] Ajouter la différenciation dans les 18 fichiers de maths/premiere

### Priorité moyenne
- [ ] Vérifier la présence de boutons `.bc` pour chaque bloc `.corr`
- [ ] Auditer les DS : barème, durée, couverture des capacités
- [ ] Vérifier la cohérence des numérotations d'exercices

### Priorité basse
- [ ] Compléter les 29 pages BTS stub avec du contenu réel
- [ ] Harmoniser le mécanisme de correction (choisir entre `<details>` et `.bc`)
- [ ] Harmoniser le format des corrections (rédaction type, niveau de détail)
- [ ] Ajouter des exercices de synthèse (multi-chapitres) en fin de progression
- [ ] Créer un script de comptage automatique `.exo` vs `.corr` pour le suivi
