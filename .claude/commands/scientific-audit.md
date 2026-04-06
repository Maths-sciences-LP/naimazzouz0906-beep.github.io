# Skill : Audit scientifique d'une page de cours

## Usage

```
/scientific-audit <chemin-fichier>
```

Exemples :
- `/scientific-audit physique-chimie/seconde/ch11/lecon.html`
- `/scientific-audit maths/terminale/ch03/lecon.html`

---

## Objectif

Vérifier la **rigueur scientifique du contenu** d'une page, indépendamment de sa structure ou de sa pédagogie.
Cet audit ne modifie aucun fichier — il produit un rapport et, si des problèmes sont identifiés, propose les corrections à apporter.

---

## Étape 1 — Lire la page

Lire le fichier HTML indiqué. Identifier :
- la matière (maths / physique-chimie)
- le niveau (Seconde / Première / Terminale / CAP / BTS)
- le chapitre et son titre

---

## Étape 2 — Extraire tous les éléments vérifiables

Parcourir le HTML et dresser la liste de **tout ce qui peut être vérifié scientifiquement** :

### 2a. Valeurs numériques
Relever chaque constante, coefficient ou valeur physique utilisée (dans les formules, tableaux, exemples) :
- conductivités λ, coefficients U, résistances Rth
- masses volumiques, chaleurs spécifiques, indices de réfraction, etc.
- toute valeur chiffrée présentée comme une référence

Pour chacune : **noter la valeur utilisée dans la page** et **calculer la valeur attendue** à partir des sources standard (tables de physique, programme officiel, données du tableau de la page elle-même si disponibles).

### 2b. Exemples numériques calculés
Relever chaque calcul présenté avec un résultat chiffré.
Refaire le calcul indépendamment et vérifier :
- que le résultat est numériquement juste
- que l'ordre de grandeur est physiquement crédible (cohérent avec la réalité)
- que les unités sont cohérentes

### 2c. Formules
Relever chaque formule présentée. Vérifier :
- que la formule est correcte dans le domaine d'application
- que les hypothèses implicites sont réalistes pour le contexte
- que les hypothèses sont explicitées (régime permanent, matériau homogène, modèle simplifié…)

### 2d. Affirmations qualitatives absolues
Relever les formulations du type :
- "le plus…" / "le meilleur…" / "le pire…"
- "toujours" / "jamais" / "dans tous les cas"
- "réduit d'un facteur X" (vérifier si ce facteur est justifié)
- "l'essentiel de…" / "principalement dû à…"
- comparaisons superlatives sans nuance

Pour chacune : évaluer si la formulation est justifiable ou si elle doit être nuancée.

### 2e. Références réglementaires et nomenclature
Vérifier que les noms de réglementations, normes et organismes sont exacts et à jour :
- RE2020 (pas RT2020, pas RT 2020)
- noms de normes ISO, NF, EN
- appellations officielles de filières et diplômes

---

## Étape 3 — Identifier les modèles sans limites explicitées

Repérer les modèles simplifiés utilisés sans que leurs limites soient mentionnées.
Exemples typiques :
- formule Rth = e/(λS) appliquée à une fenêtre réelle sans mentionner qu'elle ignore les résistances superficielles
- loi d'Ohm appliquée hors de son domaine de validité
- modèle de gaz parfait sans mention des conditions
- tout modèle dont le résultat donne un ordre de grandeur irréaliste

---

## Étape 4 — Produire le rapport

Afficher un rapport structuré de ce format :

```
## Audit scientifique : physique-chimie/seconde/ch11/lecon.html
**Chapitre** : Ch11 — Transferts thermiques et équilibre thermique
**Niveau** : 2nde Bac Pro — Physique-Chimie

---

### Valeurs numériques
| Valeur utilisée | Valeur attendue | Statut | Ligne |
|---|---|---|---|
| λ_argon = 0,017 W·m⁻¹·K⁻¹ | 0,0172 W·m⁻¹·K⁻¹ | ✅ OK | L.483 |
| U simple vitrage = 5,8 W·m⁻²·K⁻¹ | ~5,7–5,8 W·m⁻²·K⁻¹ | ✅ OK | L.493 |
| bois isole 6 à 8× mieux que le verre | 1,0/0,12 ≈ 8,3 ; 1,0/0,17 ≈ 5,9 → fourchette 6–8× | ✅ OK | L.446 |

### Exemples calculés
| Calcul | Résultat page | Résultat vérifié | Ordre de grandeur | Statut |
|---|---|---|---|---|
| Rth panneau bois pin 18mm, S=1,8 m² | 0,083 K/W | 0,018/(0,12×1,8) = 0,083 ✅ | — | ✅ OK |
| Φ fenêtre SV, U=5,8, S=1,5, ΔT=20 | 174 W | 5,8×1,5×20 = 174 ✅ | Réaliste ✅ | ✅ OK |

### Formules
| Formule | Contexte | Hypothèses explicitées ? | Statut |
|---|---|---|---|
| Rth = e/(λS) | Paroi homogène en régime permanent | Oui (bloc Attention L.314) | ✅ OK |
| Φ = U×S×ΔT | Fenêtre complète | Oui (section 6.3) | ✅ OK |

### Affirmations qualitatives
| Formulation | Évaluation | Statut |
|---|---|---|
| "améliore fortement l'isolation" (double vitrage) | Justifié (U passe de 5,8 à 1,4) | ✅ OK |
| "réduit fortement les déperditions" | Non quantifié mais prudent | ✅ OK |

### Réglementation
| Terme utilisé | Terme attendu | Statut |
|---|---|---|
| RE2020 | RE2020 | ✅ OK |

### Modèles sans limites explicitées
Aucun problème détecté.

---

### Bilan
✅ Aucun problème scientifique identifié.

--- OU ---

### Problèmes identifiés
| # | Gravité | Description | Ligne | Correction suggérée |
|---|---|---|---|---|
| 1 | HAUTE | "4 à 6 fois mieux que le verre" — pin : ×8,3, chêne : ×5,9 → fourchette correcte : 6 à 8 | L.447 | Remplacer par "6 à 8 fois" |
| 2 | MOYENNE | Modèle Rth=e/(λS) appliqué à une fenêtre sans mention des résistances superficielles | L.490 | Ajouter encadré "Limite du modèle" |
| 3 | BASSE | "RT 2020" → devrait être "RE2020" | L.485 | Remplacer partout |

### Actions recommandées
1. [HAUTE] Corriger le ratio bois/verre : "6 à 8 fois" (ligne 447)
2. [MOYENNE] Ajouter un encadré "Limite du modèle" après l'exemple section 6.3
3. [BASSE] Remplacer "RT 2020" par "RE2020" (lignes 485, 556)
```

---

## Étape 5 — Mise à jour de l'audit (optionnelle)

Si des problèmes ont été identifiés **et** que l'utilisateur confirme vouloir mettre à jour l'audit :

1. Identifier l'audit approprié :
   - `audits/audit-pedagogique-pc.md` pour les pages de physique-chimie
   - `audits/audit-pedagogique-maths.md` pour les pages de maths
2. Ajouter les problèmes identifiés dans `## Problemes identifies` avec leur gravité
3. Ajouter les corrections déjà réalisées dans `## Corrections realisees` avec la date du jour
4. Mettre à jour la date `Dernière mise à jour`

Si des corrections ont déjà été appliquées lors d'une session précédente, les déplacer vers `## Corrections realisees` plutôt que de les laisser dans `## Problemes identifies`.

---

## Étape 5 — Mettre à jour le journal des audits

Après avoir affiché le rapport, mettre à jour `audits/audit-log.md` :

1. Identifier le chapitre parent du fichier audité (ex: `physique-chimie/seconde/ch11`)
2. Chercher si ce chapitre a déjà une ligne dans le tableau
3. Si oui : mettre à jour la colonne `/scientific-audit` avec la date du jour (format `YYYY-MM-DD`) et le résultat (🔴 / 🟡 / 🟢)
4. Si non : ajouter une nouvelle ligne
5. Mettre à jour la date `Dernière mise à jour` en haut du fichier

---

## Règles

- **Ne jamais modifier le fichier audité** — seulement analyser et rapporter
- **Recalculer chaque valeur numérique** à partir de la formule et des données disponibles — ne pas faire confiance à un chiffre hérité
- **Signaler les problèmes par ordre de gravité** : CRITIQUE > HAUTE > MOYENNE > BASSE
- **Ne pas signaler comme erreur** ce qui est délibérément simplifié et correctement annoté
- Adapter le niveau d'exigence au public : un modèle simplifié est acceptable en 2nde si ses limites sont explicitées
