# run.ps1
# Ausführen in PowerShell mit:
#   .\run.ps1

Write-Output "🐍 Starte zootag.py..."
python zootag.py

Write-Output "📄 Kompiliere main.tex..."
pdflatex -interaction=nonstopmode main.tex

Write-Output "✅ Fertig! Ausgabe: main.pdf"