#!/usr/bin/env python3

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.feature_selection import f_classif


parser = argparse.ArgumentParser(
    description="Generiert einen synthetischen Datensatz mit expliziter Kovarianz- und Wichtigkeitssteuerung"
)
parser.add_argument(
    "-n",
    "--rows",
    type=int,
    default=100,
    help="Anzahl zu generierender Zeilen (Default: 100)",
)
parser.add_argument(
    "--seed",
    type=int,
    default=42,
    help="Seed fuer Reproduzierbarkeit (Default: 42)",
)
parser.add_argument(
    "-o",
    "--output",
    type=Path,
    default=Path(__file__).with_name("learning_style_classifier.csv"),
    help="Zielpfad der CSV-Datei",
)
parser.add_argument(
    "--w-lernzeit",
    type=float,
    default=0.55,
    help="Feature-Wichtigkeit fuer Lernzeit_h",
)
parser.add_argument(
    "--w-fehlzeiten",
    type=float,
    default=-0.35,
    help="Feature-Wichtigkeit fuer Fehlzeiten",
)
parser.add_argument(
    "--w-hausaufgabenquote",
    type=float,
    default=0.65,
    help="Feature-Wichtigkeit fuer Hausaufgabenquote",
)
parser.add_argument(
    "--w-vorwissen",
    type=float,
    default=0.20,
    help="Feature-Wichtigkeit fuer Vorwissen_Test",
)
parser.add_argument(
    "--corr-lf",
    type=float,
    default=-0.55,
    help="Korrelation Lernzeit_h <-> Fehlzeiten",
)
parser.add_argument(
    "--corr-lh",
    type=float,
    default=0.60,
    help="Korrelation Lernzeit_h <-> Hausaufgabenquote",
)
parser.add_argument(
    "--corr-lv",
    type=float,
    default=0.50,
    help="Korrelation Lernzeit_h <-> Vorwissen_Test",
)
parser.add_argument(
    "--corr-fh",
    type=float,
    default=-0.50,
    help="Korrelation Fehlzeiten <-> Hausaufgabenquote",
)
parser.add_argument(
    "--corr-fv",
    type=float,
    default=-0.45,
    help="Korrelation Fehlzeiten <-> Vorwissen_Test",
)
parser.add_argument(
    "--corr-hv",
    type=float,
    default=0.58,
    help="Korrelation Hausaufgabenquote <-> Vorwissen_Test",
)
parser.add_argument(
    "--std-lernzeit",
    type=float,
    default=1.6,
    help="Standardabweichung fuer Lernzeit_h",
)
parser.add_argument(
    "--std-fehlzeiten",
    type=float,
    default=2.3,
    help="Standardabweichung fuer Fehlzeiten",
)
parser.add_argument(
    "--std-hausaufgabenquote",
    type=float,
    default=0.16,
    help="Standardabweichung fuer Hausaufgabenquote",
)
parser.add_argument(
    "--std-vorwissen",
    type=float,
    default=0.70,
    help="Standardabweichung fuer Vorwissen_Test",
)
parser.add_argument(
    "--interaction-strength",
    type=float,
    default=0.65,
    help="Staerke der nichtlinearen Interaktionen",
)
parser.add_argument(
    "--noise-std",
    type=float,
    default=0.45,
    help="Rauschstaerke im Label-Score",
)
args = parser.parse_args()

if args.rows < 20:
    raise ValueError("Bitte mindestens 20 Zeilen generieren, damit die Verteilung stabil ist.")

if args.interaction_strength < 0:
    raise ValueError("interaction-strength muss >= 0 sein.")

if args.noise_std <= 0:
    raise ValueError("noise-std muss > 0 sein.")

if args.std_lernzeit <= 0 or args.std_fehlzeiten <= 0 or args.std_hausaufgabenquote <= 0 or args.std_vorwissen <= 0:
    raise ValueError("Alle Standardabweichungen muessen > 0 sein.")

rng = np.random.default_rng(args.seed)
n = args.rows

for corr in [args.corr_lf, args.corr_lh, args.corr_lv, args.corr_fh, args.corr_fv, args.corr_hv]:
    if corr <= -1.0 or corr >= 1.0:
        raise ValueError("Alle Korrelationen muessen strikt zwischen -1 und 1 liegen.")

corr_matrix = np.array(
    [
        [1.0, args.corr_lf, args.corr_lh, args.corr_lv],
        [args.corr_lf, 1.0, args.corr_fh, args.corr_fv],
        [args.corr_lh, args.corr_fh, 1.0, args.corr_hv],
        [args.corr_lv, args.corr_fv, args.corr_hv, 1.0],
    ],
    dtype=float,
)

eigenvalues = np.linalg.eigvalsh(corr_matrix)
if np.min(eigenvalues) <= 1e-8:
    raise ValueError(
        "Die angegebene Korrelationsmatrix ist nicht positiv definit. Bitte Korrelationen anpassen."
    )

std_vector = np.array(
    [
        args.std_lernzeit,
        args.std_fehlzeiten,
        args.std_hausaufgabenquote,
        args.std_vorwissen,
    ],
    dtype=float,
)

cov_matrix = np.outer(std_vector, std_vector) * corr_matrix
mu = np.array([5.4, 5.2, 0.58, 4.2], dtype=float)

latent = rng.multivariate_normal(mean=mu, cov=cov_matrix, size=n)

lernzeit_h = np.clip(latent[:, 0], 1.0, 10.0)
fehlzeiten = np.clip(np.rint(latent[:, 1]), 0, 12).astype(int)
hausaufgabenquote = np.clip(latent[:, 2], 0.15, 0.98)
vorwissen_test = np.clip(latent[:, 3], 2.3, 5.8)

x1 = (lernzeit_h - np.mean(lernzeit_h)) / (np.std(lernzeit_h) + 1e-9)
x2 = (fehlzeiten - np.mean(fehlzeiten)) / (np.std(fehlzeiten) + 1e-9)
x3 = (hausaufgabenquote - np.mean(hausaufgabenquote)) / (np.std(hausaufgabenquote) + 1e-9)
x4 = (vorwissen_test - np.mean(vorwissen_test)) / (np.std(vorwissen_test) + 1e-9)

linear_score = (
    args.w_lernzeit * x1
    + args.w_fehlzeiten * x2
    + args.w_hausaufgabenquote * x3
    + args.w_vorwissen * x4
)

interaction_score = args.interaction_strength * (
    0.7 * x1 * x3
    # - 0.8 * x2 * x4
    # + 0.45 * np.sin(1.8 * x1)
    # - 0.35 * (x2 ** 2)
)

raw_score = linear_score + interaction_score + rng.normal(0, args.noise_std, n)

cutoff = np.quantile(raw_score, 0.5)
bestanden = (raw_score > cutoff).astype(int)

df = pd.DataFrame(
    {
        "Lernzeit_h": np.round(lernzeit_h, 1),
        "Fehlzeiten": fehlzeiten,
        "Hausaufgabenquote": np.round(hausaufgabenquote, 2),
        "Vorwissen_Test": np.round(vorwissen_test, 1),
        "Bestanden": bestanden,
    }
)

args.output.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(args.output, index=False)

features = ["Lernzeit_h", "Fehlzeiten", "Hausaufgabenquote", "Vorwissen_Test"]
y = df["Bestanden"].to_numpy()

beste_acc = 0.0
bestes_merkmal = ""

for merkmal in features:
    x = df[merkmal].to_numpy()
    unique_sorted = np.unique(x)

    if unique_sorted.size == 1:
        acc1 = np.mean(y == 0)
        acc2 = np.mean(y == 1)
        feature_best = max(acc1, acc2)
    else:
        mitte = (unique_sorted[:-1] + unique_sorted[1:]) / 2
        feature_best = 0.0

        for t in mitte:
            pred_ge = (x >= t).astype(int)
            pred_lt = (x < t).astype(int)

            acc_ge = np.mean(pred_ge == y)
            acc_lt = np.mean(pred_lt == y)

            if acc_ge > feature_best:
                feature_best = acc_ge
            if acc_lt > feature_best:
                feature_best = acc_lt

    if feature_best > beste_acc:
        beste_acc = feature_best
        bestes_merkmal = merkmal

anteil_pos = float(np.mean(y))

X_for_anova = df[features].to_numpy()
f_values, p_values = f_classif(X_for_anova, y)

emp_corr = df[features].corr().to_numpy()

print(f"Datei geschrieben: {args.output}")
print(f"Zeilen: {len(df)}")
print(f"Positiver Klassenanteil: {anteil_pos:.3f}")
print(f"Beste Ein-Merkmal-Stumpfgenauigkeit: {beste_acc:.3f} ({bestes_merkmal})")
print("ANOVA F-Werte pro Merkmal:")
for i, merkmal in enumerate(features):
    print(f"  {merkmal}: F={f_values[i]:.3f}, p={p_values[i]:.3e}")

print("Ziel-Korrelationsmatrix (Input):")
print(np.round(corr_matrix, 3))
print("Empirische Korrelationsmatrix (Output):")
print(np.round(emp_corr, 3))
