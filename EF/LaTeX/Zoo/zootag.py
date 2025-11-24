from pathlib import Path
import matplotlib.pyplot as plt

# ==== Daten ====
labels = [
    "Personal",
    "Entwicklung, Logistik, Energie & Unterhalt",
    "Wareneinkauf Restaurant & Shops",
    "Besucherservice, Werbung & Marketing",
    "Verwaltung",
    "Forschung & Naturschutz",
    "Tierfutter & tierärztliche Betreuung",
]
values = [190000, 22000, 21000, 7000, 7000, 4000, 4000]

# ==== Pfad vorbereiten ====
# Ordner, in dem das Skript liegt
script_dir = Path(__file__).parent
# PDF-Datei im gleichen Ordner speichern
output_file = script_dir / "ausgaben.pdf"

# ==== Diagramm erstellen ====
plt.figure(figsize=(8, 8))
plt.pie(values, labels=labels, autopct="%.1f%%", startangle=140)
plt.title("Ausgaben pro Tag (Total: CHF 143'000.–)", fontsize=14)

# ==== Speichern ====
plt.savefig(output_file, bbox_inches="tight")
print(f"PDF gespeichert unter: {output_file}")
