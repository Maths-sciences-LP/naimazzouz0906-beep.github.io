# Audit Pédagogique

**Date** : 2026-03-16
**Dernière mise à jour** : 2026-03-16
**Périmètre** : qualité pédagogique des cours, structure, différenciation, contextes professionnels

---

## Problemes identifies

### 1. Différenciation absente en maths/premiere (18 fichiers)

**Gravité : HAUTE**

Toute la section `maths/premiere` (9 exercices.html + 9 ds.html) ne contient **aucune différenciation pédagogique** :
- Pas d'inclusion de `diff.js`
- Pas de classes `diff-socle`, `diff-standard`, `diff-appro`
- Pas de tags de niveau

**Sections avec différenciation fonctionnelle** :
- maths/terminale (22 fichiers)
- physique-chimie/premiere-iccer (20 fichiers)
- physique-chimie/premiere-era (20 fichiers)
- physique-chimie/terminale-iccer (16 fichiers)
- physique-chimie/terminale-era (16 fichiers)

**Section manquante** : `maths/premiere` — 18 fichiers à traiter.

### 2. Sigles de filière dans le contenu pédagogique

Aucune occurrence des patterns interdits (`technicien ICCER`, `technicien ERA`, `technicien MAMA`, `technicien ERA-MA`) détectée dans le contenu. Bonne pratique respectée.

**Vigilance** : vérifier aussi les formulations plus subtiles (`contexte ERA-MA`, `application ICCER`, etc.) lors d'audits futurs.

### 3. Différenciation non applicable en Seconde

Conformément à la philosophie du site, la Seconde ne nécessite pas de différenciation. Les sections `maths/seconde` et `physique-chimie/seconde` sont correctement sans diff.js.

### 4. Qualité des contextes professionnels

À vérifier systématiquement :
- Les exercices utilisent-ils des contextes variés (professionnel, sport, science, quotidien) ?
- Les situations professionnelles sont-elles réalistes et ancrées dans les métiers cibles ?
- Les classes `.situation` sont-elles utilisées pour identifier les contextes pro ?

---

## Corrections realisees

- Aucune à ce stade.

---

## Ameliorations restantes

### Priorité haute
- [ ] Ajouter diff.js et les 3 niveaux de différenciation dans `maths/premiere/ch01` à `ch09` (exercices.html)
- [ ] Ajouter diff.js et les 3 niveaux de différenciation dans `maths/premiere/ch01` à `ch09` (ds.html)

### Priorité moyenne
- [ ] Auditer la variété des contextes professionnels dans chaque section
- [ ] Vérifier que les métiers utilisés correspondent aux filières cibles (cf. tableau CLAUDE.md)
- [ ] Vérifier l'utilisation des classes pédagogiques (.def, .prop, .meth, .att, .retenir) dans tous les cours

### Priorité basse
- [ ] Vérifier la progressivité pédagogique entre les 3 niveaux (socle → standard → appro)
- [ ] Auditer la qualité des corrections : sont-elles détaillées et formatées correctement ?
- [ ] Vérifier que les lecon.html ne contiennent PAS de diff.js (conformité CLAUDE.md)
