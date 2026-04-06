"""
add_answer_lines.py — Ajoute des zones de réponse (.answer-line) aux exercices.html
                      et exercices-capacites.html.

Usage :
  python3 scripts/add_answer_lines.py maths/seconde/ch05
  python3 scripts/add_answer_lines.py maths/seconde          # tous les chapitres du niveau
  python3 scripts/add_answer_lines.py --all                  # tout le site

Règles :
  - diff-socle   → 3 lignes
  - diff-standard → 5 lignes
  - diff-appro   → 6 lignes
  - sans diff    → 4 lignes

Pour chaque exo :
  - Si <div class="zone-rep"> existe : remplace son contenu par label + answer-lines
  - Sinon : insère une <div class="zone-rep"> avant le bouton .bc
"""

import re
import sys
import glob
import os

LINES_BY_LEVEL = {
    'diff-socle': 3,
    'diff-standard': 5,
    'diff-appro': 6,
    'none': 4,
}

ANSWER_LINE = '    <span class="answer-line"></span>\n'

ZONE_REP_PATTERN = re.compile(
    r'(<div class="zone-rep">)\s*(<label>[^<]*</label>)?\s*(</div>)',
    re.DOTALL
)

BC_BUTTON_PATTERN = re.compile(
    r'(\s*<button class="bc"[^>]*>Voir la correction</button>)'
)


def build_zone_rep(n_lines):
    lines = ''.join([ANSWER_LINE] * n_lines)
    return (
        f'  <div class="zone-rep">\n'
        f'    <label>Mes calculs :</label>\n'
        f'{lines}'
        f'  </div>\n'
    )


def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Déjà traité ?
    if '<span class="answer-line"></span>' in content:
        print(f'[skip] {path}')
        return

    # Découper en blocs d'exercices pour traiter chaque exo indépendamment
    # Stratégie : traiter le fichier bloc par bloc entre les <div class="exo ...">
    # On itère sur les positions des ouvertures d'exo

    result = []
    pos = 0
    # Correspond uniquement à <div class="exo"> ou <div class="exo diff-...">
    # Exclut <div class="exo-header">, <div class="exo-num">, etc.
    # ( [^"]+)? = groupe optionnel qui commence par un espace (donc pas exo-)
    exo_open = re.compile(r'<div class="exo( [^"]+)?">')

    for m in exo_open.finditer(content):
        # Ajouter tout ce qui précède ce bloc
        result.append(content[pos:m.start()])

        # Déterminer le niveau
        classes = m.group(1) or ''
        if 'diff-socle' in classes:
            level = 'diff-socle'
        elif 'diff-standard' in classes:
            level = 'diff-standard'
        elif 'diff-appro' in classes:
            level = 'diff-appro'
        else:
            level = 'none'

        n_lines = LINES_BY_LEVEL[level]
        zone_rep_html = build_zone_rep(n_lines)

        # Trouver la fin de ce bloc exo (prochain <div class="exo ou fin de fichier)
        next_m = exo_open.search(content, m.end())
        end = next_m.start() if next_m else len(content)
        block = content[m.start():end]

        # Cas 1 : zone-rep déjà présente → remplacer son contenu
        if '<div class="zone-rep">' in block:
            new_block = ZONE_REP_PATTERN.sub(
                lambda _: (
                    f'  <div class="zone-rep">\n'
                    f'    <label>Mes calculs :</label>\n'
                    f'{"".join([ANSWER_LINE] * n_lines)}'
                    f'  </div>'
                ),
                block
            )
            result.append(new_block)
        else:
            # Cas 2 : pas de zone-rep → insérer avant le bouton .bc
            new_block = BC_BUTTON_PATTERN.sub(
                lambda m_bc: f'\n{zone_rep_html}{m_bc.group(1)}',
                block,
                count=1  # seulement le premier bouton du bloc
            )
            result.append(new_block)

        pos = end

    # Ajouter le reste (après le dernier exo)
    result.append(content[pos:])

    new_content = ''.join(result)

    if new_content == content:
        print(f'[WARN] aucun changement dans {path}')
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'[OK]   {path}')


def collect_files(arg):
    if arg == '--all':
        patterns = [
            'maths/**/exercices.html',
            'maths/**/exercices-capacites.html',
            'physique-chimie/**/exercices.html',
            'physique-chimie/**/exercices-capacites.html',
        ]
    elif os.path.isdir(arg):
        patterns = [
            f'{arg}/exercices.html',
            f'{arg}/exercices-capacites.html',
            f'{arg}/*/exercices.html',
            f'{arg}/*/exercices-capacites.html',
        ]
    else:
        # Chemin direct vers un fichier
        return [arg] if os.path.isfile(arg) else []

    files = []
    for p in patterns:
        files.extend(glob.glob(p, recursive=True))
    return sorted(set(files))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 scripts/add_answer_lines.py <chemin|--all>')
        sys.exit(1)

    files = collect_files(sys.argv[1])
    if not files:
        print('Aucun fichier trouvé.')
        sys.exit(1)

    ok = 0
    for path in files:
        before = open(path, encoding='utf-8').read()
        process_file(path)
        after = open(path, encoding='utf-8').read()
        if before != after:
            ok += 1

    print(f'\n{ok} fichier(s) modifié(s).')
