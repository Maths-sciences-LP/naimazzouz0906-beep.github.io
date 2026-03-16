# Audit Global du Site Pédagogique

**Date** : 2026-03-16
**Dernière mise à jour** : 2026-03-16
**Périmètre** : ensemble du site maths-sciences-lp.github.io

---

## Vue d'ensemble

| Indicateur | Valeur |
|---|---|
| Pages HTML totales | 477 |
| Sections (matière/niveau) | 8 (+1 BTS) |
| Chapitres couverts | 89 |
| Simulations interactives | 63 |
| Pages de cours (lecon.html) | 89 |
| Pages d'exercices (exercices.html) | 89 |
| Pages de DS (ds.html) | 89 |
| Programmes officiels (PDF) | 10+ |

### Couverture par section

| Section | Chapitres attendus | Chapitres existants | Couverture |
|---|---|---|---|
| maths/seconde | 14 | 14 | 100 % |
| maths/premiere | 9 | 9 | 100 % |
| maths/terminale | 11 | 11 | 100 % |
| physique-chimie/seconde | 14 | 14 | 100 % |
| physique-chimie/premiere-iccer | 10 | 10 | 100 % |
| physique-chimie/premiere-era | 10 | 10 | 100 % |
| physique-chimie/terminale-iccer | 11 (CLAUDE.md) | 8 | 73 % |
| physique-chimie/terminale-era | 8 | 8 | 100 % |

Chaque chapitre existant possède les 3 types de pages (lecon, exercices, ds).

---

## Problemes identifies

1. **Chapitres manquants en terminale ICCER** : CLAUDE.md indique ch01-ch11, mais seuls ch01-ch08 existent. Soit le programme a été réduit (mettre à jour CLAUDE.md), soit 3 chapitres restent à créer.

2. **Chemins absolus cassés** : 61 fichiers utilisent `src="/nav.js"` et 37 fichiers utilisent `href="/nav.css"` au lieu de chemins relatifs (`../../../nav.js`). Ces pages fonctionnent en local mais le chargement dépend du serveur.

3. **Simulations non liées** : 56 simulations sur 63 ne sont référencées dans aucune page de cours — elles sont orphelines et difficilement accessibles par les élèves.

4. **Différenciation absente en maths/premiere** : les 18 fichiers (exercices + DS) de maths/premiere n'incluent pas diff.js et n'utilisent pas la différenciation pédagogique.

5. **Corrections incomplètes** : certaines pages d'exercices ont un déséquilibre entre le nombre d'exercices (.exo) et de corrections (.corr), ce qui suggère des corrections manquantes.

6. **29 pages BTS stub** : dans `maths/bts/`, 29 fichiers (exercices.html et ds.html) ne contiennent qu'un placeholder "Ce devoir surveillé est en cours de rédaction". Les chapitres ch03-ch18 sont partiellement ou totalement incomplets.

---

## Corrections realisees

_(Section à compléter au fil des corrections)_

- Aucune correction effectuée à ce stade — cet audit constitue l'état initial de référence.

---

## Ameliorations restantes

### Priorité haute
- [ ] Corriger les 61 chemins absolus `/nav.js` → `../../../nav.js`
- [ ] Corriger les 37 chemins absolus `/nav.css` → `../../../nav.css`
- [ ] Clarifier le nombre de chapitres attendus en physique-chimie/terminale-iccer

### Priorité moyenne
- [ ] Ajouter diff.js et la différenciation dans maths/premiere (9 exercices + 9 DS)
- [ ] Lier les 56 simulations orphelines aux pages de cours correspondantes
- [ ] Compléter les corrections manquantes dans les pages d'exercices

### Priorité basse
- [ ] Compléter les 29 pages BTS stub (exercices et DS)
- [ ] Harmoniser les conventions de nommage entre sections
- [ ] Mettre en place un script de vérification automatique (CI)
