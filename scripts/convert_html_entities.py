#!/usr/bin/env python3
"""Convertit les entités HTML en caractères UTF-8 dans les fichiers .html.

Préserve les 4 entités sémantiques : &lt; &gt; &amp; &nbsp; &quot; &apos;
Convertit toutes les autres entités présentes dans le repo (63 identifiées).

Usage: python3 scripts/convert_html_entities.py [chemin]
       python3 scripts/convert_html_entities.py maths/cap
       python3 scripts/convert_html_entities.py --dry-run maths/cap
"""

import sys
import os
import re

ENTITY_MAP = {
    # Lettres françaises accentuées (minuscules)
    "eacute": "é", "egrave": "è", "agrave": "à",
    "ecirc": "ê", "ocirc": "ô", "ucirc": "û", "acirc": "â", "icirc": "î",
    "ccedil": "ç", "oelig": "œ",
    "euml": "ë", "iuml": "ï", "ugrave": "ù",
    # Lettres françaises accentuées (majuscules)
    "Eacute": "É", "Egrave": "È", "Agrave": "À",
    "Ecirc": "Ê", "Ocirc": "Ô", "Ucirc": "Û", "Acirc": "Â", "Icirc": "Î",
    "Ccedil": "Ç", "OElig": "Œ",
    "Euml": "Ë", "Iuml": "Ï", "Ugrave": "Ù",
    # Apostrophe typographique
    "rsquo": "’",
    # Tirets
    "ndash": "–", "mdash": "—",
    # Symboles
    "deg": "°", "euro": "€", "sect": "§", "middot": "·",
    "hellip": "…", "laquo": "«", "raquo": "»",
    "bull": "•", "micro": "µ",
    # Maths
    "times": "×", "divide": "÷", "plusmn": "±", "minus": "−",
    "sdot": "⋅", "ne": "≠", "le": "≤", "ge": "≥",
    "asymp": "≈", "sim": "∼", "cap": "∩", "cup": "∪",
    "radic": "√", "prime": "′", "Prime": "″",
    "parallel": "∥", "perp": "⊥",
    "oslash": "ø", "Oslash": "Ø",
    "approx": "≈", "dot": "⋅",
    "aelig": "æ", "AElig": "Æ",
    # Flèches
    "larr": "←", "rarr": "→", "harr": "↔",
    "uarr": "↑", "darr": "↓",
    "nearr": "↗", "nwarr": "↖", "searr": "↘", "swarr": "↙",
    "circlearrowleft": "↺", "circlearrowright": "↻",
    # Validation
    "check": "✓", "checkmark": "✓",
    # Lettres grecques (minuscules, en utilisant le bloc Greek/Coptic)
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ",
    "epsilon": "ε", "eta": "η", "lambda": "λ", "mu": "μ",
    "nu": "ν", "omega": "ω", "phi": "φ", "pi": "π",
    "rho": "ρ", "sigma": "σ", "tau": "τ", "theta": "θ", "xi": "ξ",
    # Lettres grecques (majuscules)
    "Alpha": "Α", "Beta": "Β", "Gamma": "Γ", "Delta": "Δ",
    "Epsilon": "Ε", "Eta": "Η", "Lambda": "Λ", "Mu": "Μ",
    "Nu": "Ν", "Omega": "Ω", "Phi": "Φ", "Pi": "Π",
    "Rho": "Ρ", "Sigma": "Σ", "Tau": "Τ", "Theta": "Θ", "Xi": "Ξ",
    # Flèches doubles (logique mathématique)
    "rArr": "⇒", "lArr": "⇐", "hArr": "⇔", "dArr": "⇓", "uArr": "⇑",
    # Espaces typographiques
    "ensp": " ", "emsp": " ", "thinsp": " ",
    # Soft hyphen (invisible, marque de césure conditionnelle)
    "shy": "­",
}

# Entités à PRESERVER (sémantique HTML obligatoire)
PRESERVE = {"lt", "gt", "amp", "nbsp", "quot", "apos"}

ENTITY_RE = re.compile(r"&([a-zA-Z]+);")


def convert_text(text: str) -> tuple[str, int, set[str]]:
    """Retourne (texte_converti, nb_remplacements, entites_inconnues)."""
    n = 0
    unknown = set()

    def repl(match):
        nonlocal n
        name = match.group(1)
        if name in PRESERVE:
            return match.group(0)
        if name in ENTITY_MAP:
            n += 1
            return ENTITY_MAP[name]
        unknown.add(name)
        return match.group(0)

    new_text = ENTITY_RE.sub(repl, text)
    return new_text, n, unknown


def process_file(path: str, dry_run: bool = False) -> tuple[int, set[str]]:
    with open(path, encoding="utf-8") as f:
        original = f.read()
    new_text, n, unknown = convert_text(original)
    if n > 0 and not dry_run:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_text)
    return n, unknown


def main():
    args = sys.argv[1:]
    dry_run = False
    if args and args[0] == "--dry-run":
        dry_run = True
        args = args[1:]
    if not args:
        print("Usage: convert_html_entities.py [--dry-run] <path>")
        sys.exit(1)

    target = args[0]
    files = []
    if os.path.isfile(target):
        files = [target]
    elif os.path.isdir(target):
        for root, _, names in os.walk(target):
            for name in names:
                if name.endswith(".html"):
                    files.append(os.path.join(root, name))
    else:
        print(f"Chemin introuvable : {target}")
        sys.exit(1)

    total = 0
    touched = 0
    all_unknown = set()
    for f in sorted(files):
        n, unknown = process_file(f, dry_run=dry_run)
        all_unknown.update(unknown)
        if n > 0:
            touched += 1
            total += n
            mark = "[dry-run]" if dry_run else "[ok]"
            print(f"  {mark} {f} : {n} entités")

    print()
    print(f"=== Résumé ===")
    print(f"Fichiers parcourus : {len(files)}")
    print(f"Fichiers modifiés  : {touched}")
    print(f"Entités converties : {total}")
    if all_unknown:
        print(f"Entités INCONNUES (non converties, non sémantiques) :")
        for u in sorted(all_unknown):
            print(f"  &{u};")


if __name__ == "__main__":
    main()
