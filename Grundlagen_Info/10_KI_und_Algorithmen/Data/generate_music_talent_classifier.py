#!/usr/bin/env python3

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.feature_selection import f_classif


parser = argparse.ArgumentParser(
    description="Generiert einen synthetischen Datensatz für Musiktalent-Klassifikation mit expliziter Kovarianz- und Wichtigkeitssteuerung"
)
parser.add_argument(
    "-n",
    "--rows",
    type=int,
    default=150,
    help="Anzahl zu generierender Zeilen (Default: 150)",
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
    default=Path(__file__).with_name("music_talent_classifier.csv"),
    help="Zielpfad der CSV-Datei",
)
parser.add_argument(
    "--w-gehör",
    type=float,
    default=0.60,
    help="Feature-Wichtigkeit fuer Gehörtraining_Score",
)
parser.add_argument(
    "--w-rhythmus",
    type=float,
    default=0.55,
    help="Feature-Wichtigkeit fuer Rhythmusgefühl",
)
parser.add_argument(
    "--w-geschwindigkeit",
    type=float,
    default=0.50,
    help="Feature-Wichtigkeit fuer Spielgeschwindigkeit_NPM",
)
parser.add_argument(
    "--w-gedächtnis",
    type=float,
    default=0.45,
    help="Feature-Wichtigkeit fuer Musikalisches_Gedächtnis",
)
parser.add_argument(
    "--w-erfahrung",
    type=float,
    default=0.25,
    help="Feature-Wichtigkeit fuer Musikunterricht_Jahre",
)
parser.add_argument(
    "--corr-gh",
    type=float,
    default=0.65,
    help="Korrelation Gehörtraining_Score <-> Rhythmusgefühl",
)
parser.add_argument(
    "--corr-gs",
    type=float,
    default=0.55,
    help="Korrelation Gehörtraining_Score <-> Spielgeschwindigkeit_NPM",
)
parser.add_argument(
    "--corr-gg",
    type=float,
    default=0.70,
    help="Korrelation Gehörtraining_Score <-> Musikalisches_Gedächtnis",
)
parser.add_argument(
    "--corr-ge",
    type=float,
    default=0.40,
    help="Korrelation Gehörtraining_Score <-> Musikunterricht_Jahre",
)
parser.add_argument(
    "--corr-hs",
    type=float,
    default=0.60,
    help="Korrelation Rhythmusgefühl <-> Spielgeschwindigkeit_NPM",
)
parser.add_argument(
    "--corr-hg",
    type=float,
    default=0.58,
    help="Korrelation Rhythmusgefühl <-> Musikalisches_Gedächtnis",
)
parser.add_argument(
    "--corr-he",
    type=float,
    default=0.35,
    help="Korrelation Rhythmusgefühl <-> Musikunterricht_Jahre",
)
parser.add_argument(
    "--corr-sg",
    type=float,
    default=0.50,
    help="Korrelation Spielgeschwindigkeit_NPM <-> Musikalisches_Gedächtnis",
)
parser.add_argument(
    "--corr-se",
    type=float,
    default=0.42,
    help="Korrelation Spielgeschwindigkeit_NPM <-> Musikunterricht_Jahre",
)
parser.add_argument(
    "--corr-ge-",
    type=float,
    default=0.48,
    help="Korrelation Musikalisches_Gedächtnis <-> Musikunterricht_Jahre",
)
parser.add_argument(
    "--std-gehör",
    type=float,
    default=1.2,
    help="Standardabweichung fuer Gehörtraining_Score",
)
parser.add_argument(
    "--std-rhythmus",
    type=float,
    default=1.3,
    help="Standardabweichung fuer Rhythmusgefühl",
)
parser.add_argument(
    "--std-geschwindigkeit",
    type=float,
    default=15.0,
    help="Standardabweichung fuer Spielgeschwindigkeit_NPM",
)
parser.add_argument(
    "--std-gedächtnis",
    type=float,
    default=1.1,
    help="Standardabweichung fuer Musikalisches_Gedächtnis",
)
parser.add_argument(
    "--std-erfahrung",
    type=float,
    default=1.8,
    help="Standardabweichung fuer Musikunterricht_Jahre",
)
parser.add_argument(
    "--interaction-strength",
    type=float,
    default=0.60,
    help="Staerke der nichtlinearen Interaktionen",
)
parser.add_argument(
    "--noise-std",
    type=float,
    default=0.50,
    help="Rauschstaerke im Label-Score",
)
args = parser.parse_args()

if args.rows < 30:
    raise ValueError("Bitte mindestens 30 Zeilen generieren, damit die Verteilung stabil ist.")

if args.interaction_strength < 0:
    raise ValueError("interaction-strength muss >= 0 sein.")

if args.noise_std <= 0:
    raise ValueError("noise-std muss > 0 sein.")

if args.std_gehör <= 0 or args.std_rhythmus <= 0 or args.std_geschwindigkeit <= 0 or args.std_gedächtnis <= 0 or args.std_erfahrung <= 0:
    raise ValueError("Alle Standardabweichungen muessen > 0 sein.")

rng = np.random.default_rng(args.seed)
n = args.rows

corr_values = [
    args.corr_gh, args.corr_gs, args.corr_gg, args.corr_ge,
    args.corr_hs, args.corr_hg, args.corr_he,
    args.corr_sg, args.corr_se,
    args.corr_ge_
]

for corr in corr_values:
    if corr <= -1.0 or corr >= 1.0:
        raise ValueError("Alle Korrelationen muessen strikt zwischen -1 und 1 liegen.")

corr_matrix = np.array(
    [
        [1.0, args.corr_gh, args.corr_gs, args.corr_gg, args.corr_ge],
        [args.corr_gh, 1.0, args.corr_hs, args.corr_hg, args.corr_he],
        [args.corr_gs, args.corr_hs, 1.0, args.corr_sg, args.corr_se],
        [args.corr_gg, args.corr_hg, args.corr_sg, 1.0, args.corr_ge_],
        [args.corr_ge, args.corr_he, args.corr_se, args.corr_ge_, 1.0],
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
        args.std_gehör,
        args.std_rhythmus,
        args.std_geschwindigkeit,
        args.std_gedächtnis,
        args.std_erfahrung,
    ],
    dtype=float,
)

cov_matrix = np.outer(std_vector, std_vector) * corr_matrix
mu = np.array([6.8, 7.2, 85.0, 7.5, 4.5], dtype=float)

latent = rng.multivariate_normal(mean=mu, cov=cov_matrix, size=n)

gehörtraining = np.clip(latent[:, 0], 2.0, 10.0)
rhythmusgefühl = np.clip(latent[:, 1], 2.0, 10.0)
spielgeschwindigkeit = np.clip(latent[:, 2], 40.0, 150.0)
musikalisches_gedächtnis = np.clip(latent[:, 3], 2.0, 10.0)
musikunterricht_jahre = np.clip(np.rint(latent[:, 4]), 0, 12).astype(int)

x1 = (gehörtraining - np.mean(gehörtraining)) / (np.std(gehörtraining) + 1e-9)
x2 = (rhythmusgefühl - np.mean(rhythmusgefühl)) / (np.std(rhythmusgefühl) + 1e-9)
x3 = (spielgeschwindigkeit - np.mean(spielgeschwindigkeit)) / (np.std(spielgeschwindigkeit) + 1e-9)
x4 = (musikalisches_gedächtnis - np.mean(musikalisches_gedächtnis)) / (np.std(musikalisches_gedächtnis) + 1e-9)
x5 = (musikunterricht_jahre - np.mean(musikunterricht_jahre)) / (np.std(musikunterricht_jahre) + 1e-9)

linear_score = (
    args.w_gehör * x1
    + args.w_rhythmus * x2
    + args.w_geschwindigkeit * x3
    + args.w_gedächtnis * x4
    + args.w_erfahrung * x5
)

interaction_score = args.interaction_strength * (
    0.65 * x1 * x4
    + 0.55 * x2 * x3
    - 0.40 * np.abs(x1 - x2)
)

raw_score = linear_score + interaction_score + rng.normal(0, args.noise_std, n)

q33 = np.quantile(raw_score, 0.33)
q67 = np.quantile(raw_score, 0.67)
talent_level = np.zeros(n, dtype=int)
talent_level[(raw_score >= q33) & (raw_score < q67)] = 1
talent_level[raw_score >= q67] = 2

talent_labels = {0: "Anfänger", 1: "Mittelstufe", 2: "Fortgeschrittene"}

df = pd.DataFrame(
    {
        "Gehörtraining_Score": np.round(gehörtraining, 1),
        "Rhythmusgefühl": np.round(rhythmusgefühl, 1),
        "Spielgeschwindigkeit_NPM": np.round(spielgeschwindigkeit, 0).astype(int),
        "Musikalisches_Gedächtnis": np.round(musikalisches_gedächtnis, 1),
        "Musikunterricht_Jahre": musikunterricht_jahre,
        "Talent_Niveau": talent_level,
    }
)

args.output.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(args.output, index=False)

features = ["Gehörtraining_Score", "Rhythmusgefühl", "Spielgeschwindigkeit_NPM", "Musikalisches_Gedächtnis", "Musikunterricht_Jahre"]
y = df["Talent_Niveau"].to_numpy()

beste_acc = 0.0
bestes_merkmal = ""

for merkmal in features:
    x = df[merkmal].to_numpy()
    unique_sorted = np.unique(x)

    if unique_sorted.size == 1:
        feature_best = np.max([np.mean(y == k) for k in np.unique(y)])
    else:
        mitte = (unique_sorted[:-1] + unique_sorted[1:]) / 2
        feature_best = 0.0

        for t in mitte:
            pred = np.digitize(x, [t])
            acc = np.mean(pred == (y > 0).astype(int))

            if acc > feature_best:
                feature_best = acc

    if feature_best > beste_acc:
        beste_acc = feature_best
        bestes_merkmal = merkmal

class_distribution = {k: float(np.mean(y == k)) for k in np.unique(y)}

X_for_anova = df[features].to_numpy()
f_values, p_values = f_classif(X_for_anova, y)

emp_corr = df[features].corr().to_numpy()

print(f"Datei geschrieben: {args.output}")
print(f"Zeilen: {len(df)}")
print(f"Klassenverteilung: {class_distribution}")
print(f"Beste Ein-Merkmal-Genauigkeit: {beste_acc:.3f} ({bestes_merkmal})")
print("ANOVA F-Werte pro Merkmal:")
for i, merkmal in enumerate(features):
    print(f"  {merkmal}: F={f_values[i]:.3f}, p={p_values[i]:.3e}")

print("\nZiel-Korrelationsmatrix (Input):")
print(np.round(corr_matrix, 3))
print("\nEmpirische Korrelationsmatrix (Output):")
print(np.round(emp_corr, 3))

print("\nTalent-Niveau-Mapping:")
for level, label in talent_labels.items():
    print(f"  {level} -> {label}")
