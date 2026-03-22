#!/usr/bin/env python3
"""Check sequential numbering of exercises in all exercices.html files.

Verifies:
1. Numbers start at 1
2. Numbers are sequential (no gaps, no duplicates)
3. Order follows: all socle exercises first, then standard, then appro
"""

import re
import os
import glob

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Collect all exercices.html excluding bts/
patterns = [
    os.path.join(BASE, "maths", "**", "exercices.html"),
    os.path.join(BASE, "physique-chimie", "**", "exercices.html"),
]

files = []
for p in patterns:
    files.extend(glob.glob(p, recursive=True))

# Exclude bts
files = [f for f in files if "/bts/" not in f]
files.sort()

# Regex to find exo-num spans and surrounding diff class
# We need to find the parent div's diff class and the exercise number together
EXO_NUM_RE = re.compile(r'<span\s+class="exo-num">\s*Exercice\s+(\d+)\s*</span>')
# Match a div with class containing exo and optionally diff-*
DIV_DIFF_RE = re.compile(r'<div\s+class="[^"]*\bexo\b[^"]*\bdiff-(socle|standard|appro)\b[^"]*"')
DIV_EXO_RE = re.compile(r'<div\s+class="[^"]*\bexo\b[^"]*"')

LEVEL_ORDER = {"socle": 0, "standard": 1, "appro": 2, None: -1}

issues_found = 0
files_with_issues = 0
clean_files = 0

for filepath in files:
    relpath = os.path.relpath(filepath, BASE)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract exercises with their line numbers and diff levels
    # Strategy: scan line by line, track current diff level from enclosing div
    lines = content.split("\n")
    exercises = []  # list of (exo_number, diff_level, line_number)

    current_diff = None
    # Track div nesting to know when we leave a diff block
    # Simpler approach: find each exo-num and look backwards for the nearest div.exo
    for i, line in enumerate(lines, 1):
        m = EXO_NUM_RE.search(line)
        if m:
            exo_num = int(m.group(1))
            # Look backwards for the nearest div with class="exo ..."
            diff_level = None
            for j in range(i - 1, max(0, i - 6), -1):
                prev_line = lines[j - 1] if j > 0 else ""
                dm = DIV_DIFF_RE.search(prev_line)
                if dm:
                    diff_level = dm.group(1)
                    break
                # Also check if it's a plain exo div (no diff class)
                if DIV_EXO_RE.search(prev_line) and not DIV_DIFF_RE.search(prev_line):
                    diff_level = None
                    break
            exercises.append((exo_num, diff_level, i))

    if not exercises:
        continue

    file_issues = []

    # Check 1: Numbers start at 1
    numbers = [e[0] for e in exercises]
    if numbers[0] != 1:
        file_issues.append(f"  Does not start at 1 (starts at {numbers[0]})")

    # Check 2: Sequential (no gaps, no duplicates)
    expected = list(range(1, len(numbers) + 1))
    if numbers != expected:
        # Find specific issues
        seen = set()
        for idx, n in enumerate(numbers):
            if n in seen:
                file_issues.append(f"  DUPLICATE: Exercice {n} (line {exercises[idx][2]})")
            seen.add(n)

        # Check for gaps
        for i in range(len(numbers) - 1):
            if numbers[i + 1] != numbers[i] + 1:
                if numbers[i + 1] > numbers[i] + 1:
                    missing = list(range(numbers[i] + 1, numbers[i + 1]))
                    file_issues.append(
                        f"  GAP: after Exercice {numbers[i]} (line {exercises[i][2]}), "
                        f"next is Exercice {numbers[i+1]} (line {exercises[i+1][2]}), "
                        f"missing: {missing}"
                    )
                elif numbers[i + 1] <= numbers[i]:
                    file_issues.append(
                        f"  NON-SEQUENTIAL: Exercice {numbers[i]} (line {exercises[i][2]}) "
                        f"followed by Exercice {numbers[i+1]} (line {exercises[i+1][2]})"
                    )

    # Check 3: Order should be socle -> standard -> appro
    levels = [e[1] for e in exercises]
    # Filter out None (exercises without diff class)
    diff_exercises = [(e[0], e[1], e[2]) for e in exercises if e[1] is not None]

    if diff_exercises:
        diff_levels = [e[1] for e in diff_exercises]
        # Check that all socle come before all standard, which come before all appro
        last_level_seen = -1
        order_ok = True
        first_violation = None
        for exo_num, level, line_num in diff_exercises:
            level_idx = LEVEL_ORDER[level]
            if level_idx < last_level_seen:
                order_ok = False
                if first_violation is None:
                    first_violation = (exo_num, level, line_num)
            last_level_seen = max(last_level_seen, level_idx)

        if not order_ok:
            exo_num, level, line_num = first_violation
            file_issues.append(
                f"  ORDER VIOLATION: Exercice {exo_num} is '{level}' (line {line_num}) "
                f"but appears after a higher-level exercise"
            )
            # Show the full order for context
            order_summary = []
            for e in diff_exercises:
                order_summary.append(f"Ex{e[0]}={e[1]}")
            file_issues.append(f"  Level order: {', '.join(order_summary)}")

    if file_issues:
        files_with_issues += 1
        issues_found += len(file_issues)
        print(f"\n{'='*70}")
        print(f"ISSUES in: {relpath}")
        print(f"  Exercises found: {len(exercises)} ({', '.join(str(n) for n in numbers)})")
        for issue in file_issues:
            print(issue)
    else:
        clean_files += 1

print(f"\n{'='*70}")
print(f"SUMMARY")
print(f"  Total files checked: {len(files)}")
print(f"  Files with issues: {files_with_issues}")
print(f"  Clean files: {clean_files}")
print(f"  Total issues: {issues_found}")
