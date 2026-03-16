# Audit Technique

**Date** : 2026-03-16
**Dernière mise à jour** : 2026-03-16
**Périmètre** : HTML, CSS, JavaScript, chemins, accessibilité

---

## Problemes identifies

### 1. Chemins absolus cassés — nav.js (61 fichiers)

**Gravité : CRITIQUE**

61 fichiers utilisent `<script src="/nav.js"></script>` au lieu du chemin relatif `../../../nav.js`. Cela peut empêcher le chargement de la navigation selon la configuration du serveur.

**Sections touchées** : principalement `maths/terminale/` et une partie de `physique-chimie/`.

**Fichiers concernés** (exemples) :
- `maths/terminale/ch01/lecon.html` à `ch11/lecon.html`
- `maths/terminale/ch01/exercices.html` à `ch11/exercices.html`
- `maths/terminale/ch01/ds.html` à `ch11/ds.html`
- Plusieurs fichiers en physique-chimie

### 2. Chemins absolus cassés — nav.css (37 fichiers)

**Gravité : CRITIQUE**

37 fichiers utilisent `<link rel="stylesheet" href="/nav.css">` au lieu de `../../../nav.css`. Aucun fichier du site n'utilise le chemin relatif correct pour nav.css — les 37 concernés sont tous en chemin absolu.

### 3. Lien cassé dans maths/seconde/ch01/lecon.html

**Gravité : HAUTE**

Ligne 859 : `<a href="ch01_exos.html">` pointe vers un fichier inexistant. Le fichier correct est `exercices.html`.

### 4. Aucune redéfinition CSS inline détectée

Les classes de `styles.css` (`.def`, `.prop`, `.att`, `.meth`) ne sont redéfinies dans aucun `<style>` inline — bonne pratique respectée.

### 5. MathJax correctement inclus

Toutes les pages de cours vérifées incluent le script MathJax v3. Pas de page sans MathJax détectée.

### 6. Attributs HTML de base corrects

- `lang="fr"` : présent sur toutes les pages
- `<meta charset="UTF-8">` : présent partout
- `<meta name="viewport">` : présent partout

### 7. print.css inclus

Les pages incluent `<link rel="stylesheet" href="../../../print.css" media="print">` — impression correctement gérée.

---

## Corrections realisees

- Aucune à ce stade.

---

## Ameliorations restantes

### Corrections immédiates
- [ ] Remplacer `src="/nav.js"` par `src="../../../nav.js"` dans 61 fichiers
- [ ] Remplacer `href="/nav.css"` par `href="../../../nav.css"` dans 37 fichiers
- [ ] Corriger le lien `ch01_exos.html` → `exercices.html` dans `maths/seconde/ch01/lecon.html`

### Améliorations recommandées
- [ ] Créer un script de validation des chemins (lint HTML) pour détecter les chemins absolus
- [ ] Ajouter un test CI qui vérifie que tous les liens internes pointent vers des fichiers existants
- [ ] Vérifier l'accessibilité (attributs `alt` sur les images éventuelles, rôles ARIA sur les boutons interactifs)
- [ ] Vérifier la cohérence des balises `<title>` sur l'ensemble du site
