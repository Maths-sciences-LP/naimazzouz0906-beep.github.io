# Memo Claude Code - Skills & Commandes

Fiche de reference rapide pour le projet **Maths & Sciences LP**.

---

## 1. Skills de generation de contenu

| Commande | Description | Argument attendu |
|---|---|---|
| `/new-chapter` | Creer la structure complete d'un nouveau chapitre (dossier + fichiers vides) | Section et numero (ex: `maths/seconde/ch15`) |
| `/generate-lecon` | Generer un cours (`lecon.html`) | Chemin du chapitre |
| `/generate-exercices` | Generer des exercices differencies (`exercices.html`) | Chemin du chapitre |
| `/generate-exercices-capacites` | Generer des exercices par capacites du programme (`exercices-capacites.html`) | Chemin du chapitre |
| `/generate-ds` | Generer un devoir surveille differencie (`ds.html`) | Chemin du chapitre |
| `/generate-qcm` | Generer un QCM interactif (`qcm.html`) | Chemin du chapitre |
| `/generate-interro` | Generer une interrogation ecrite (`interro.html`) | Chemin du chapitre |
| `/generate-fiche` | Generer une fiche de revision / memo (`fiche.html`) | Chemin du chapitre |
| `/generate-activite` | Generer une activite de decouverte (`activite.html`) | Chemin du chapitre |
| `/generate-simulation` | Generer une simulation interactive | Chemin du chapitre ou theme |

### Exemple d'utilisation

```
/generate-lecon maths/seconde/ch08
/generate-ds physique-chimie/premiere-iccer/ch03
/generate-qcm maths/terminale/ch05
```

---

## 2. Skills d'audit et qualite

Les audits s'utilisent **en chaine**, du plus large au plus precis :

```
/section-audit <section>          -> tableau de bord macro (tous les chapitres)
      |
/audit-chapter <chapitre>         -> completude + sigles (1 chapitre)
      |
/check-quality <chapitre>         -> qualite technique et contenu (1 chapitre)
      |
/scientific-audit <fichier>       -> rigueur scientifique (1 page)
```

| Commande | Portee | Ce qu'il verifie | Modele conseille |
|---|---|---|---|
| `/section-audit` | Section entiere (ex: `maths/seconde`) | Completude, visuels, differenciation, sigles | Opus |
| `/audit-chapter` | 1 chapitre | Fichiers manquants, contenu vide, sigles interdits | Sonnet |
| `/check-quality` | 1 chapitre | Technique (nav.js, CSS...), donnees, refs orphelines, mini-exo, visuels, QCM | Sonnet |
| `/scientific-audit` | 1 page (lecon.html) | Valeurs numeriques, calculs, formules, modeles, reglementation | Sonnet |
| `/check-sigles` | 1 chapitre | Sigles de filiere utilises comme noms de metiers | Sonnet |

### Exemple d'utilisation

```
/section-audit maths/seconde
/audit-chapter physique-chimie/terminale-iccer/ch04
/check-quality maths/premiere/ch07
/scientific-audit maths/seconde/ch03/lecon.html
/check-sigles physique-chimie/premiere-era/ch02
```

---

## 3. Skills de maintenance

| Commande | Description |
|---|---|
| `/update-audit` | Mettre a jour un fichier d'audit apres corrections |
| `/css-cleanup` | Nettoyer les styles CSS inline (deplacer vers styles.css) |
| `/simplify` | Relire le code modifie pour reutilisation, qualite et efficacite |

---

## 4. Scripts de maintenance (terminal)

A lancer manuellement dans le terminal :

| Commande | Description |
|---|---|
| `python3 scripts/check_chapters.py` | Verifier la completude de tous les chapitres |
| `python3 scripts/check_chapters.py --missing` | Afficher seulement les chapitres incomplets |
| `python3 scripts/check_chapters.py --section maths/bts` | Verifier une section precise |
| `python3 scripts/extract_css.py` | Nettoyer les doublons CSS inline vers styles.css |
| `python3 scripts/add_print_css.py` | Ajouter print.css aux pages qui ne l'ont pas |
| `python3 scripts/link_simulations.py` | Verifier/ajouter les liens simulations <-> chapitres |
| `python3 scripts/check_exo_numbering.py` | Verifier la numerotation des exercices |
| `node scripts/generate-pdf.js` | Generer les PDF des cours |

---

## 5. Prompts pedagogiques de reference

Consulter ces fichiers dans `/prompts/` avant de generer du contenu :

### Structure de contenu

| Fichier | Quand le consulter |
|---|---|
| `prompts/regles-communes.md` | **Toujours** — regles partagees (donnees, tableaux, animations, SVG) |
| `prompts/prompt-cours.md` | Avant de generer un cours |
| `prompts/prompt-exercices.md` | Avant de generer des exercices |
| `prompts/prompt-exercices-capacites.md` | Avant de generer des exercices par capacites |
| `prompts/prompt-ds.md` | Avant de generer un DS |
| `prompts/prompt-qcm-interro.md` | Avant de generer un QCM ou une interro |
| `prompts/prompt-activite.md` | Avant de generer une activite |
| `prompts/prompt-fiche.md` | Avant de generer une fiche |
| `prompts/prompt-simulation.md` | Avant de generer une simulation |
| `prompts/prompt-bts.md` | Pour les pages BTS |
| `prompts/prompt-superviseur.md` | Supervision globale du projet |

### Contextes professionnels par filiere

| Fichier | Filiere |
|---|---|
| `prompts/prompt-filiere-2mama.md` | Seconde MAMA (menuiserie/agencement) |
| `prompts/prompt-filiere-premiere-iccer.md` | Premiere ICCER (chauffage/energie) |
| `prompts/prompt-filiere-premiere-era.md` | Premiere ERA-MA (bois/agencement) |
| `prompts/prompt-filiere-ticcer.md` | Terminale ICCER |
| `prompts/prompt-filiere-era-ma.md` | Terminale ERA/MA |
| `prompts/prompt-filiere-cap-mit.md` | CAP MIT (installations thermiques) |
| `prompts/prompt-filiere-cap-ebeniste.md` | CAP Ebeniste |
| `prompts/prompt-filiere-cap-sdg.md` | CAP SDG (signaletique) |
| `prompts/prompt-filiere-bma-ebeniste.md` | BMA Ebeniste |
| `prompts/prompt-filiere-bma-arts-graphiques.md` | BMA Arts Graphiques |
| `prompts/prompt-filiere-eeb-tgt.md` | EEB / TGT (batiment, geometre) |
| `prompts/prompt-filiere-mee.md` | MEE (maintenance energetique) |

---

## 6. Workflow type

### Creer un chapitre complet

```
1. /new-chapter maths/seconde/ch15
2. /generate-lecon maths/seconde/ch15
3. /generate-exercices maths/seconde/ch15
4. /generate-ds maths/seconde/ch15
5. /generate-fiche maths/seconde/ch15
6. /generate-qcm maths/seconde/ch15
7. /generate-interro maths/seconde/ch15
8. /generate-activite maths/seconde/ch15
9. /check-quality maths/seconde/ch15
```

### Auditer une section

```
1. /section-audit maths/seconde           <- vue d'ensemble
2. /audit-chapter maths/seconde/ch03      <- chapitre prioritaire
3. /check-quality maths/seconde/ch03      <- qualite technique
4. /scientific-audit maths/seconde/ch03/lecon.html  <- rigueur scientifique
5. (corrections...)
6. /update-audit                           <- mise a jour de l'audit
```

### Verifier les sigles interdits

```
/check-sigles physique-chimie/premiere-iccer/ch05
```

> **Rappel :** Ne jamais utiliser ICCER, ERA, MA, ERA-MA, MAMA comme noms de metiers dans le contenu pedagogique. Utiliser les vrais noms de metiers (menuisier, chauffagiste, etc.).

---

## 7. Fichiers d'audit (feuille de route)

Les audits dans `/audits/` pilotent le travail. Les consulter avant de generer du contenu :

| Fichier | Dimension |
|---|---|
| `audits/audit-global.md` | Vue d'ensemble, couverture par section |
| `audits/audit-technique.md` | HTML, CSS, JS, chemins, accessibilite |
| `audits/audit-programmes.md` | Conformite programmes officiels |
| `audits/audit-pedagogique.md` | Differenciation, contextes pro (synthese) |
| `audits/audit-pedagogique-maths.md` | Detail pedagogique maths |
| `audits/audit-pedagogique-pc.md` | Detail pedagogique physique-chimie |
| `audits/audit-exercices.md` | Corrections, DS, completude |
| `audits/audit-simulations.md` | Simulations interactives |
| `audits/audit-uniformisation.md` | Uniformisation des formats |

---

## 8. Raccourcis utiles Claude Code

| Action | Commande |
|---|---|
| Aide generale | `/help` |
| Basculer en mode rapide | `/fast` |
| Effacer le contexte | `/clear` |

---

*Memo genere le 2026-04-06 pour le projet maths-sciences-lp.github.io*
