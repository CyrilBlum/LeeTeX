from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, plot_tree


BASE = Path(__file__).resolve().parents[1]
DATA_DIR = BASE / "Data"
FIG_DIR = BASE / "Figures"


def _load_classification_data():
    df = pd.read_csv(DATA_DIR / "learning_style_classifier.csv")
    X = df[["Lernzeit_h", "Fehlzeiten"]]
    y = df["Bestanden"]
    return X, y


def plot_decision_tree() -> None:
    X, y = _load_classification_data()
    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(X, y)

    plt.figure(figsize=(10, 6))
    plot_tree(
        model,
        feature_names=["Lernzeit_h", "Fehlzeiten"],
        class_names=["Nicht bestanden", "Bestanden"],
        filled=True,
        rounded=True,
        fontsize=9,
    )
    plt.tight_layout()
    plt.savefig(FIG_DIR / "decision_tree_structure.pdf")
    plt.close()


def plot_random_forest_importance() -> None:
    X, y = _load_classification_data()
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    importances = model.feature_importances_

    plt.figure(figsize=(6, 4))
    plt.bar(["Lernzeit_h", "Fehlzeiten"], importances, color="#C44E52")
    plt.ylabel("Importance")
    plt.title("Random Forest: Feature-Importances")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "random_forest_feature_importance.pdf")
    plt.close()


def _plot_decision_boundary(clf, title: str, out_file: str) -> None:
    X, y = _load_classification_data()
    clf.fit(X, y)

    x_min, x_max = X["Lernzeit_h"].min() - 0.5, X["Lernzeit_h"].max() + 0.5
    y_min, y_max = X["Fehlzeiten"].min() - 1, X["Fehlzeiten"].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300), np.linspace(y_min, y_max, 300))
    grid = pd.DataFrame(
        np.c_[xx.ravel(), yy.ravel()],
        columns=["Lernzeit_h", "Fehlzeiten"],
    )
    Z = clf.predict(grid).reshape(xx.shape)

    plt.figure(figsize=(7, 5))
    plt.contourf(xx, yy, Z, alpha=0.25, cmap="coolwarm")
    plt.scatter(X["Lernzeit_h"], X["Fehlzeiten"], c=y, cmap="coolwarm", edgecolor="k")
    plt.xlabel("Lernzeit (h)")
    plt.ylabel("Fehlzeiten")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(FIG_DIR / out_file)
    plt.close()


def plot_svm_boundary() -> None:
    _plot_decision_boundary(SVC(kernel="rbf", C=1.0, gamma="scale"), "SVM-Entscheidungsgrenze", "svm_boundary.pdf")


def plot_knn_boundary() -> None:
    _plot_decision_boundary(KNeighborsClassifier(n_neighbors=5), "KNN-Entscheidungsgrenze (k=5)", "knn_boundary.pdf")


def plot_regression_prediction() -> None:
    df = pd.read_csv(DATA_DIR / "apartment_prices.csv")
    X = df[["Wohnflaeche_m2"]]
    y = df["Preis_CHF"]

    model = LinearRegression()
    model.fit(X, y)

    x_line = np.linspace(X.min().iloc[0], X.max().iloc[0], 100)
    x_line_df = pd.DataFrame({"Wohnflaeche_m2": x_line})
    y_line = model.predict(x_line_df)

    plt.figure(figsize=(7, 5))
    plt.scatter(X, y, label="Datenpunkte")
    plt.plot(x_line_df["Wohnflaeche_m2"], y_line, color="red", label="Regressionslinie")
    plt.xlabel("Wohnfläche (m²)")
    plt.ylabel("Preis (CHF)")
    plt.title("Prediction mit linearer Regression")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIG_DIR / "regression_prediction.pdf")
    plt.close()


def main() -> None:
    plot_decision_tree()
    plot_random_forest_importance()
    plot_svm_boundary()
    plot_knn_boundary()
    plot_regression_prediction()

    # quick sanity check on one model
    X, y = _load_classification_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    _ = accuracy_score(y_test, clf.predict(X_test))


if __name__ == "__main__":
    main()
