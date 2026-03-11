# Prompt de référence — Génération de pages d'exercices

## Rôle
Ce fichier définit les règles à appliquer pour générer les pages d'exercices et les devoirs surveillés du site pédagogique.

---

## Niveau cible
**Bac Professionnel** (Seconde, Première, Terminale)

---

## Structure obligatoire d'une page d'exercices

1. **Titre de la série d'exercices** — lié au cours correspondant
2. **Rappel de cours** (optionnel) — quelques lignes ou formules essentielles
3. **Exercices progressifs** — du niveau 1 (accessible) au niveau 3 (expert)
4. **Correction détaillée** — disponible sous forme masquée ou sur page séparée

---

## Progression par niveau de difficulté

### Niveau 1 — Application directe
- Exercice guidé, étapes indiquées
- Une seule notion mobilisée
- Valeurs numériques simples
- Contexte professionnel simple et familier

### Niveau 2 — Transfert
- Exercice moins guidé
- Combinaison de 2 notions
- Contexte professionnel réaliste
- Une ou deux étapes intermédiaires à trouver

### Niveau 3 — Résolution de problème
- Exercice ouvert avec mise en situation complète
- Plusieurs notions combinées
- Données à extraire d'un document ou d'un schéma
- Proche d'une situation professionnelle réelle

---

## Contextualisation des exercices

- Chaque exercice doit être **ancré dans un contexte professionnel** de la filière concernée
- Utiliser les **situations, métiers et objets techniques** définis dans le prompt de filière
- Les valeurs numériques doivent être **réalistes** et **cohérentes** avec le domaine professionnel

---

## Structure d'un exercice

Chaque exercice doit comporter :
- **Numéro et titre** de l'exercice
- **Mise en situation** (2 à 5 lignes de contexte professionnel)
- **Données fournies** — tableau ou liste des valeurs connues avec unités
- **Questions** — numérotées, avec indication du niveau de difficulté si nécessaire
- **Espace de réponse** — zone visible pour les élèves (HTML : `<div class="zone-reponse">`)
- **Correction détaillée** — accessible via bouton ou page dédiée, avec toutes les étapes rédigées

---

## Zone de réponse

- Matérialisée visuellement dans la page HTML
- Peut inclure un champ texte ou une zone de calcul interactif si pertinent
- Doit être clairement distinguée de l'énoncé

---

## Correction détaillée

- Chaque étape de calcul est **expliquée en français**
- Les formules utilisées sont **rappelées** avant le calcul numérique
- Le résultat est **interprété** dans le contexte professionnel
- Unités toujours présentes et vérifiées

---

## Contraintes techniques HTML

- Utilisation des classes CSS existantes du site
- Formules mathématiques rendues avec **MathJax** ou **KaTeX**
- Correction masquée par défaut avec un bouton "Afficher la correction"
- Accessible et lisible sur mobile

---

## Cohérence pédagogique

- Les exercices doivent **suivre la progression du cours** associé
- Le niveau 1 doit être accessible à tous les élèves
- Le niveau 3 peut servir de différenciation ou d'approfondissement
- Pour les devoirs surveillés : équilibrer les niveaux (environ 50 % niveau 1, 35 % niveau 2, 15 % niveau 3)

---

## Références à combiner

Avant de générer des exercices, lire aussi :
- `prompt-cours.md` pour s'assurer de la cohérence avec le cours
- Le prompt de filière correspondant (`prompt-filiere-ticcer.md`, `prompt-filiere-era-ma.md` ou `prompt-filiere-2mama.md`)
