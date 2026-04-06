#!/usr/bin/env python3
"""Convert a Markdown file to PDF using markdown + weasyprint."""
import sys
import markdown
from weasyprint import HTML

if len(sys.argv) < 3:
    print("Usage: python3 md2pdf.py input.md output.pdf")
    sys.exit(1)

md_path, pdf_path = sys.argv[1], sys.argv[2]

with open(md_path, encoding="utf-8") as f:
    md_text = f.read()

html_body = markdown.markdown(md_text, extensions=["tables", "fenced_code", "codehilite"])

html_full = f"""<!DOCTYPE html>
<html lang="fr">
<head><meta charset="utf-8">
<style>
@page {{
  size: A4;
  margin: 2cm 1.8cm;
  @bottom-center {{ content: counter(page) " / " counter(pages); font-size: 9px; color: #888; }}
}}
body {{
  font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  font-size: 11pt;
  line-height: 1.5;
  color: #1a1a1a;
}}
h1 {{
  font-size: 20pt;
  color: #0056b3;
  border-bottom: 3px solid #0056b3;
  padding-bottom: 8px;
  margin-bottom: 20px;
}}
h2 {{
  font-size: 14pt;
  color: #0056b3;
  margin-top: 24px;
  border-bottom: 1px solid #bee3f8;
  padding-bottom: 4px;
}}
h3 {{
  font-size: 12pt;
  color: #333;
  margin-top: 16px;
}}
table {{
  border-collapse: collapse;
  width: 100%;
  margin: 12px 0;
  font-size: 10pt;
}}
th {{
  background: #0056b3;
  color: white;
  padding: 6px 10px;
  text-align: left;
  font-weight: 600;
}}
td {{
  padding: 5px 10px;
  border-bottom: 1px solid #e0e0e0;
}}
tr:nth-child(even) td {{
  background: #f7faff;
}}
code {{
  background: #f0f4f8;
  padding: 1px 5px;
  border-radius: 3px;
  font-size: 9.5pt;
  font-family: "Fira Code", "Consolas", monospace;
}}
pre {{
  background: #f0f4f8;
  padding: 10px 14px;
  border-radius: 6px;
  font-size: 9pt;
  line-height: 1.4;
  overflow-x: auto;
  border-left: 3px solid #0056b3;
}}
pre code {{
  background: none;
  padding: 0;
}}
blockquote {{
  border-left: 3px solid #f0ad4e;
  padding: 8px 14px;
  margin: 12px 0;
  background: #fffbf0;
  font-style: italic;
}}
hr {{
  border: none;
  border-top: 1px solid #ddd;
  margin: 20px 0;
}}
em {{ color: #555; }}
</style>
</head>
<body>{html_body}</body>
</html>"""

HTML(string=html_full).write_pdf(pdf_path)
print(f"PDF genere : {pdf_path}")
