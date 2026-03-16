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

### 3. Boutons "Voir la correction" (.bc)

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
- [ ] Harmoniser le format des corrections (rédaction type, niveau de détail)
- [ ] Ajouter des exercices de synthèse (multi-chapitres) en fin de progression
- [ ] Créer un script de comptage automatique `.exo` vs `.corr` pour le suivi
