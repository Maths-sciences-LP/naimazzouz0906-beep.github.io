# Règles communes — Visuels et contenu pédagogique

Ces règles s'appliquent à **toutes les pages du site** (exercices, DS, interro, QCM, exercices-capacités, leçon). Elles sont résumées en tête de chaque prompt sous "⚠ Interdits absolus".

---

## 1. Règle données uniquement

**Un visuel dans un exercice, DS, interro ou QCM montre uniquement les données brutes fournies à l'élève.**

Il ne doit **jamais** contenir :
- L'équation à construire (ex : `<td>18,50x + 22 = 207</td>`)
- La valeur inconnue ou la solution (ex : `<td>x = 10 panneaux</td>`)
- Un point d'intersection tracé que l'élève doit déterminer
- Une droite que l'élève doit tracer lui-même
- Une ligne de tableau "Équation :", "Inconnue :", "Résultat :"

Il doit servir de **support de compréhension**, jamais de **support de correction**.

> **Règle mnémotechnique :** *"Ce que l'élève a le droit de voir sur son énoncé, et rien de plus."*

### Exemples

**Interdit :**
```html
<table>
  <tr><th>Prix unitaire</th><td>18,50 €</td></tr>
  <tr><th>Frais de livraison</th><td>22 €</td></tr>
  <tr><th>Total facturé</th><td>207 €</td></tr>
  <tr><th>Équation</th><td>18,50x + 22 = 207</td></tr>  ← INTERDIT
  <tr><th>Solution</th><td>x = 10</td></tr>              ← INTERDIT
</table>
```

**Autorisé :**
```html
<table class="full">
  <thead><tr><th>Donnée</th><th>Valeur</th></tr></thead>
  <tbody>
    <tr><td>Prix unitaire</td><td>18,50 €</td></tr>
    <tr><td>Frais de livraison</td><td>22 €</td></tr>
    <tr><td>Total facturé</td><td>207 €</td></tr>
  </tbody>
</table>
<!-- Les questions posent ensuite : "Écrire l'équation", "Résoudre", etc. -->
```

**Interdit :**
```html
<svg>
  <!-- droite tracée avec intersection marquée à (3 ; 0) -->
  <circle cx="150" cy="80" r="4" fill="red"/>  ← INTERDIT : solution visible
  <text>x = 3</text>                            ← INTERDIT
</svg>
```

**Autorisé :**
```html
<svg>
  <!-- repère vierge avec axes et graduations uniquement -->
  <line .../>  <!-- axe x -->
  <line .../>  <!-- axe y -->
  <!-- AUCUNE droite tracée, AUCUN point solution -->
</svg>
```

---

## 2. Tableaux de données (proactive)

**Dès qu'un exercice présente 3 valeurs numériques ou plus (prix, mesures, quantités, paramètres), les regrouper dans un `<table class="full">` avant les questions** — même si le texte les cite déjà.

Ne pas attendre que l'énoncé dise "le tableau ci-dessous". Si les données sont dispersées dans le texte, les consolider en tableau.

```html
<table class="full" style="margin:8px 0 14px;font-size:.92em;max-width:360px">
  <thead><tr><th>Donnée</th><th>Valeur</th></tr></thead>
  <tbody>
    <tr><td>Prix unitaire</td><td>18,50 €</td></tr>
    <tr><td>Frais de livraison</td><td>22 €</td></tr>
    <tr><td>Total facturé</td><td>207 €</td></tr>
  </tbody>
</table>
```

---

## 3. Jamais de référence sans figure

Si l'énoncé dit **"le graphique ci-dessous"**, **"l'oscillogramme suivant"**, **"le schéma ci-contre"** ou **"à partir de la courbe"** — la figure **DOIT** être présente dans la page.

Ne jamais décrire textuellement un graphique que l'élève doit lire sans fournir la figure.

---

## 4. Animations Canvas

Les pages du site sont **dual-use** (écran + impression).

| Élément | Leçon | Exercices / DS / Interro / QCM / Capacités | Simulations |
|---|---|---|---|
| SVG statique | ✓ | ✓ prioritaire | ✓ |
| Chart.js (rendu une fois) | ✓ | ✓ acceptable | ✓ |
| Canvas animé (`requestAnimationFrame`) | ✓ (1-2 max, rôle pédagogique clair) | ✗ interdit | ✓ |
| Boutons modifiant la figure | ✓ | ✗ interdit | ✓ |

**Dans les exercices/DS/interro/QCM/capacités :** pas de `requestAnimationFrame`, `setInterval`, ni boutons qui modifient la figure. L'élève observe, lit, calcule.

---

## 5. Conventions SVG

Ces couleurs s'appliquent à tous les SVG du site (sauf simulations qui ont leurs propres styles) :

| Élément | Valeur |
|---|---|
| Fond des formes | `fill="#ebf5ff"` |
| Contour / traits principaux | `stroke="#0056b3"` |
| Longueurs inconnues (dashed) | `stroke="#c53030" stroke-dasharray="4,3"` |
| Texte / labels | `fill="#555"` |
| Grille de fond | `stroke="#e5e7eb" stroke-width="0.5"` |
| Axes | `stroke="#374151" stroke-width="1.5"` |

Toujours inclure `viewBox` et `xmlns="http://www.w3.org/2000/svg"`. Toujours ajouter un `<figcaption>` descriptif.
