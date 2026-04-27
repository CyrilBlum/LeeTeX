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
import seaborn as sns



BASE = Path(__file__).resolve().parents[1]
DATA_DIR = BASE / "Data"
FIG_DIR = BASE / "Figures"

X_COLS = ["Lernzeit_h", "Fehlzeiten", "Hausaufgabenquote", "Vorwissen_Test"]
Y_COL = "Bestanden"
CLASS_NAMES = ["Ja", "Nein"]

def _load_classification_data():
    df = pd.read_csv(DATA_DIR / "learning_style_classifier.csv")
    X = df[X_COLS]
    y = df[Y_COL]
    return X, y, df


def plot_decision_tree(X, y, max_depth: int = 3) -> None:
    model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    model.fit(X, y)

    plt.figure(figsize=(10, 6))
    plot_tree(
        model,
        feature_names=X_COLS,
        class_names=CLASS_NAMES,
        filled=True,
        rounded=True,
        fontsize=9,
    )
    plt.tight_layout()
    plt.savefig(FIG_DIR / "decision_tree_structure.pdf")
    plt.close()


def plot_decision_tree_overfitting(X, y) -> None:
    model = DecisionTreeClassifier(max_depth=None, random_state=42)
    model.fit(X, y)

    plt.figure(figsize=(15, 12))
    plot_tree(
        model,
        feature_names=X_COLS,
        class_names=CLASS_NAMES,
        filled=True,
        rounded=True,
        fontsize=7,
    )
    plt.tight_layout()
    plt.savefig(FIG_DIR / "decision_tree_overfitting.pdf")
    plt.close()


def plot_decision_tree_overfitting_issue() -> None:
    """Erzeuge drei separate Boundary-Plots fuer flachen, moderaten und tiefen Baum."""

    X_df, y_series, _ = _load_classification_data()
    X = X_df[["Lernzeit_h", "Hausaufgabenquote"]].to_numpy()
    y = y_series.to_numpy()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.35, random_state=42, stratify=y
    )

    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.08, X[:, 1].max() + 0.08
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 350), np.linspace(y_min, y_max, 350))
    grid = np.c_[xx.ravel(), yy.ravel()]

    models = [
        {
            "key": "shallow",
            "depth": 1,
            "title": "Flacher Baum (max_depth=1)",
            "subtitle": "Ein einzelner Split kann die Klassen nicht perfekt trennen.",
            "out": "decision_tree_overfitting_shallow.pdf",
        },
        {
            "key": "moderate",
            "depth": 3,
            "title": "Moderat tiefer Baum (max_depth=5)",
            "subtitle": "Guter Kompromiss: flexible Grenze mit bester Test-Accuracy.",
            "out": "decision_tree_overfitting_moderate.pdf",
        },
        {
            "key": "deep",
            "depth": None,
            "title": "Sehr tiefer Baum (max_depth=None)",
            "subtitle": "Perfektes Training, aber deutlich trainingsdatenspezifisch.",
            "out": "decision_tree_overfitting_deep.pdf",
        },
    ]

    test_scores = {}

    for spec in models:
        model = DecisionTreeClassifier(max_depth=spec["depth"], random_state=42)
        model.fit(X_train, y_train)

        # Exportiere den zugehoerigen Baum zur jeweiligen Boundary-Abbildung.
        plt.figure(figsize=(9, 6))
        plot_tree(
            model,
            feature_names=["Lernzeit_h", "Hausaufgabenquote"],
            class_names=["Klasse 0", "Klasse 1"],
            filled=True,
            rounded=True,
            fontsize=8,
        )
        plt.tight_layout()
        plt.savefig(FIG_DIR / f"decision_tree_overfitting_{spec['key']}_tree.pdf")
        plt.close()

        Z = model.predict(grid).reshape(xx.shape)
        train_acc = accuracy_score(y_train, model.predict(X_train))
        test_acc = accuracy_score(y_test, model.predict(X_test))
        test_scores[spec["key"]] = test_acc

        plt.figure(figsize=(8, 6))
        plt.contourf(xx, yy, Z, alpha=0.25, cmap="coolwarm")

        plt.scatter(
            X_train[y_train == 0, 0],
            X_train[y_train == 0, 1],
            c="#1f77b4",
            edgecolor="k",
            s=55,
            marker="o",
            label="Train Klasse 0",
        )
        plt.scatter(
            X_train[y_train == 1, 0],
            X_train[y_train == 1, 1],
            c="#d62728",
            edgecolor="k",
            s=55,
            marker="o",
            label="Train Klasse 1",
        )
        plt.scatter(
            X_test[y_test == 0, 0],
            X_test[y_test == 0, 1],
            c="#1f77b4",
            edgecolor="k",
            s=90,
            marker="*",
            label="Test Klasse 0",
        )
        plt.scatter(
            X_test[y_test == 1, 0],
            X_test[y_test == 1, 1],
            c="#d62728",
            edgecolor="k",
            s=90,
            marker="*",
            label="Test Klasse 1",
        )

        plt.xlabel("Lernzeit (h)")
        plt.ylabel("Hausaufgabenquote")
        plt.title(
            f"{spec['title']}\nTrain-Acc: {train_acc:.1%} | Test-Acc: {test_acc:.1%}\n{spec['subtitle']}",
            fontsize=10,
        )
        plt.grid(True, alpha=0.25)
        plt.legend(loc="best")
        plt.tight_layout()
        plt.savefig(FIG_DIR / spec["out"], dpi=150)
        plt.close()

    print(
        "Decision-Tree-Test-Accuracies "
        f"(shallow/moderate/deep): {test_scores['shallow']:.4f} / "
        f"{test_scores['moderate']:.4f} / {test_scores['deep']:.4f}"
    )


def plot_random_forest_importance(X, y) -> None:
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    importances = model.feature_importances_

    plt.figure(figsize=(6, 4))
    plt.bar(X_COLS, importances, color="#C44E52")
    plt.ylabel("Importance")
    plt.title("Random Forest: Feature-Importances")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "random_forest_feature_importance.pdf")
    plt.close()


def _plot_decision_boundary(clf, title: str, out_file: str) -> None:
    X, y, _ = _load_classification_data()
    X = X[["Lernzeit_h", "Fehlzeiten"]]
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


def plot_svm_boundary(X, y, margin=1.0) -> None:
    """Visualisiere SVM mit Entscheidungsgrenze, Margin und Support Vectors."""

    X = X[["Lernzeit_h", "Fehlzeiten"]]
    
    # Trainiere SVM
    model = SVC(kernel="rbf", C=margin, gamma="scale")
    model.fit(X, y)
    
    # Erstelle Gitter für Entscheidungsgrenze
    x_min, x_max = X["Lernzeit_h"].min() - 0.5, X["Lernzeit_h"].max() + 0.5
    y_min, y_max = X["Fehlzeiten"].min() - 1, X["Fehlzeiten"].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300), np.linspace(y_min, y_max, 300))
    grid = pd.DataFrame(
        np.c_[xx.ravel(), yy.ravel()],
        columns=["Lernzeit_h", "Fehlzeiten"],
    )
    
    # Vorhersagen und Entscheidungsfunktion
    Z = model.predict(grid).reshape(xx.shape)
    Z_decision = model.decision_function(grid).reshape(xx.shape)
    
    # Plotte
    plt.figure(figsize=(8, 6))
    
    # Hintergrund: Klassifikationsbereiche
    plt.contourf(xx, yy, Z, alpha=0.25, cmap="coolwarm", levels=1)
    
    # Margin: Konturlinien bei decision_function = +1 und -1
    plt.contour(xx, yy, Z_decision, levels=[0], linewidths=2, colors="black")
    plt.contour(xx, yy, Z_decision, levels=[-1, 1], linewidths=1.5, colors="black", linestyles="--", alpha=0.5)
    
    # Datenpunkte
    plt.scatter(X["Lernzeit_h"], X["Fehlzeiten"], c=y, cmap="coolwarm", edgecolor="k", s=100, label="Datenpunkte")
    
    # Support Vectors hervorheben
    support_vectors = model.support_
    plt.scatter(X.iloc[support_vectors]["Lernzeit_h"], 
                X.iloc[support_vectors]["Fehlzeiten"],
                s=200, linewidth=2, edgecolor="gold", 
                facecolors="none", label="Support Vectors")
    
    plt.xlabel("Lernzeit (h)")
    plt.ylabel("Fehlzeiten")
    plt.title("SVM: Entscheidungsgrenze mit Margin und Support Vectors")
    plt.legend(loc="best")
    plt.tight_layout()
    plt.savefig(FIG_DIR / f"svm_boundary_{margin}.pdf")
    plt.close()


def plot_knn_boundary(n_neighbors: int) -> None:
    _plot_decision_boundary(KNeighborsClassifier(n_neighbors=n_neighbors), f"KNN-Entscheidungsgrenze (k={n_neighbors})", f"knn_boundary_{n_neighbors}.pdf")


def plot_kernel_trick() -> None:
    """Visualisiere den Kernel Trick: nichtlinear trennbare Daten werden durch
    Kernel-Transformation in einen höherdimensionalen Raum gebracht, wo sie
    linear trennbar werden."""
    
    # Erstelle XOR-ähnliche Daten (nicht linear trennbar)
    np.random.seed(42)
    n_samples = 100
    
    # Cluster 1: oben-links und unten-rechts (Klasse 0)
    X1_topleft = np.random.randn(n_samples // 4, 2) * 0.3 + np.array([-1.5, 1.5])
    X1_bottomright = np.random.randn(n_samples // 4, 2) * 0.3 + np.array([1.5, -1.5])
    X1 = np.vstack([X1_topleft, X1_bottomright])
    y1 = np.zeros(n_samples // 2)
    
    # Cluster 2: oben-rechts und unten-links (Klasse 1)
    X2_topright = np.random.randn(n_samples // 4, 2) * 0.3 + np.array([1.5, 1.5])
    X2_bottomleft = np.random.randn(n_samples // 4, 2) * 0.3 + np.array([-1.5, -1.5])
    X2 = np.vstack([X2_topright, X2_bottomleft])
    y2 = np.ones(n_samples // 2)
    
    X = np.vstack([X1, X2])
    y = np.hstack([y1, y2])
    
    # RBF-Kernel-Transformation (vereinfachte Darstellung)
    # phi(x) = exp(-gamma * ||x||^2) für mehrere Zentren
    gamma = 0.5
    
    # Wähle Kernelzentren
    centers = np.array([[-1.5, 1.5], [1.5, 1.5], [1.5, -1.5], [-1.5, -1.5]])
    
    # Berechne RBF-Features
    rbf_features = np.zeros((len(X), len(centers)))
    for i, center in enumerate(centers):
        distances = np.sum((X - center) ** 2, axis=1)
        rbf_features[:, i] = np.exp(-gamma * distances)
    
    # Erstelle Visualisierung
    fig = plt.figure(figsize=(14, 5))
    
    # Subplot 1: Original-Raum (2D, nicht linear trennbar)
    ax1 = fig.add_subplot(131)
    scatter1 = ax1.scatter(X[y == 0, 0], X[y == 0, 1], c='#1f77b4', label='Klasse 0', s=50, alpha=0.7, edgecolors='k')
    scatter2 = ax1.scatter(X[y == 1, 0], X[y == 1, 1], c='#ff7f0e', label='Klasse 1', s=50, alpha=0.7, edgecolors='k')
    ax1.set_xlabel('Feature 1')
    ax1.set_ylabel('Feature 2')
    ax1.set_title('Original-Raum (2D)\nnicht linear trennbar')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-2.5, 2.5)
    ax1.set_ylim(-2.5, 2.5)
    
    # Subplot 2: Transformierter Raum (2D Projektion der RBF-Features)
    ax2 = fig.add_subplot(132)
    scatter3 = ax2.scatter(rbf_features[y == 0, 0], rbf_features[y == 0, 1], 
                          c='#1f77b4', label='Klasse 0', s=50, alpha=0.7, edgecolors='k')
    scatter4 = ax2.scatter(rbf_features[y == 1, 0], rbf_features[y == 1, 1], 
                          c='#ff7f0e', label='Klasse 1', s=50, alpha=0.7, edgecolors='k')
    
    # Versuche, eine trennende Linie zu zeichnen
    ax2.set_xlabel('RBF-Feature 1')
    ax2.set_ylabel('RBF-Feature 2')
    ax2.set_title('Kernel-Raum (2D Projektion)\nbesser trennbar')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Subplot 3: Vergleich der Trennbarkeit
    ax3 = fig.add_subplot(133)
    
    # Trainiere SVM mit linearem und RBF-Kernel
    from sklearn.model_selection import cross_val_score
    
    X_scaled = (X - X.mean(axis=0)) / (X.std(axis=0) + 1e-6)
    
    svm_linear = SVC(kernel='linear', C=1.0)
    svm_rbf = SVC(kernel='rbf', C=1.0, gamma=gamma)
    
    linear_accuracy = cross_val_score(svm_linear, X_scaled, y, cv=5).mean()
    rbf_accuracy = cross_val_score(svm_rbf, X_scaled, y, cv=5).mean()
    
    kernels = ['Linearer Kernel\n(Original-Raum)', 'RBF-Kernel\n(Transformierter Raum)']
    accuracies = [linear_accuracy, rbf_accuracy]
    colors = ['#d62728', '#2ca02c']
    
    bars = ax3.bar(kernels, accuracies, color=colors, alpha=0.7, edgecolor='k', linewidth=2)
    ax3.set_ylabel('Cross-Validation Accuracy')
    ax3.set_title('Vergleich: Kernel-Trick Effekt')
    ax3.set_ylim([0, 1.0])
    
    # Werte auf den Balken schreiben
    for bar, acc in zip(bars, accuracies):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{acc:.1%}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(FIG_DIR / "kernel_trick.pdf", dpi=150)
    plt.close()


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


def main():
    # load data once and reuse for all plots
    X, y, _ = _load_classification_data()

    # Decision Trees mit verschiedenen Tiefen und Feature-Importances
    plot_decision_tree(X, y, max_depth=3)
    plot_decision_tree_overfitting(X, y)
    plot_decision_tree_overfitting_issue()

    # Random Forest Feature-Importances
    plot_random_forest_importance(X, y)

    # SVM 
    for margin in [0.1, 1.0, 10.0]:
        plot_svm_boundary(X, y, margin=margin)
    plot_kernel_trick()

    # kNN mit verschiedenen k-Werten
    for k in [1, 5, 15, 50]:
        plot_knn_boundary(n_neighbors=k)
    
    # Regression Prediction
    plot_regression_prediction()

    # # quick sanity check on one model
    X, y, _ = _load_classification_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    _ = accuracy_score(y_test, clf.predict(X_test))


if __name__ == "__main__":
    main()
