#!/bin/bash
set -e  # Skript bricht ab, wenn ein Befehl fehlschlägt

echo "Starte zootag.py..."
python3 zootag.py

echo "Kompiliere main.tex..."
lualatex -synctex=1 -interaction=nonstopmode main.tex
biber main
lualatex -synctex=1 -interaction=nonstopmode main.tex
lualatex -synctex=1 -interaction=nonstopmode main.tex

echo "Fertig! Ausgabe: main.pdf"