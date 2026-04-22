"""
Visualisierung der PageRank-Algorithmus-Schritte als Sequenz von PDF-Dateien und GIF.
Zeigt, wie sich die PageRank-Werte bei jeder Iteration ändern.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd

try:
    from PIL import Image
except ImportError:
    Image = None


BASE = Path(__file__).resolve().parents[0]
FIG_DIR = BASE


def setup_network():
    """Netzwerk-Setup für PageRank-Visualisierung."""
    seiten = ['A', 'B', 'C', 'D']
    links = np.array([
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 0],
    ], dtype=float)
    return seiten, links


def build_graph(links, seiten):
    """Erstelle NetworkX-Graph aus Linkmatrix."""
    G = nx.DiGraph()
    G.add_nodes_from(seiten)
    
    for quelle in range(len(seiten)):
        for ziel in range(len(seiten)):
            if links[quelle, ziel] > 0:
                G.add_edge(seiten[quelle], seiten[ziel])
    
    return G


def plot_pagerank_step(G, pagerank_values, seiten, iteration, max_iterations, figsize=(10, 8)):
    """Visualisiere einen Schritt des PageRank-Algorithmus."""
    
    # Layout mit spring layout
    pos = nx.spring_layout(G, seed=42, k=2, iterations=50)
    
    # Normalisiere PageRank-Werte für Farbe und Größe
    pr_values = [pagerank_values[s] for s in seiten]
    pr_min, pr_max = min(pr_values), max(pr_values)
    pr_norm = [(v - pr_min) / (pr_max - pr_min + 1e-6) for v in pr_values]
    
    # Knotengröße basierend auf PageRank
    node_sizes = [1000 + 3000 * val for val in pr_norm]
    
    # Farbe basierend auf PageRank (dunkelrot = hoch, hellgelb = niedrig)
    node_colors = plt.cm.YlOrRd(pr_norm)
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Zeichne Kanten mit Pfeilen
    nx.draw_networkx_edges(
        G, pos,
        edge_color='gray',
        arrows=True,
        arrowsize=20,
        arrowstyle='->',
        connectionstyle='arc3,rad=0.1',
        width=2,
        ax=ax
    )
    
    # Zeichne Knoten
    nx.draw_networkx_nodes(
        G, pos,
        node_color=node_colors,
        node_size=node_sizes,
        ax=ax
    )
    
    # Zeichne Labels
    nx.draw_networkx_labels(
        G, pos,
        font_size=14,
        font_weight='bold',
        ax=ax
    )
    
    # Titel
    title = f"PageRank-Iteration {iteration}/{max_iterations}"
    ax.set_title(title, fontsize=16, fontweight='bold')
    
    # Legende mit Werten
    legend_text = "PageRank-Werte:\n"
    for i, s in enumerate(sorted(seiten)):
        legend_text += f"{s}: {pagerank_values[s]:.4f}\n"
    
    ax.text(0.98, 0.02, legend_text, transform=ax.transAxes,
            fontsize=11, verticalalignment='bottom', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
            family='monospace')
    
    ax.axis('off')
    plt.tight_layout()
    
    return fig


def run_pagerank_with_visualization():
    """Führe PageRank aus und speichere Visualisierungen für jeden Schritt."""
    
    seiten, links = setup_network()
    G = build_graph(links, seiten)
    
    # PageRank-Parameter
    n = len(seiten)
    d = 0.85
    outdegree = links.sum(axis=1)
    pagerank = {s: 1/n for s in seiten}
    
    # Speichere Verlauf
    history = []
    history.append(pagerank.copy())
    
    # Iterationen
    max_iterations = 100
    for iteration in range(max_iterations):
        neuer_pagerank = {s: (1 - d) / n for s in seiten}
        
        for quelle_idx in range(n):
            quelle = seiten[quelle_idx]
            if outdegree[quelle_idx] > 0:
                contribution = d * pagerank[quelle] / outdegree[quelle_idx]
                for ziel_idx in range(n):
                    if links[quelle_idx, ziel_idx] > 0:
                        ziel = seiten[ziel_idx]
                        neuer_pagerank[ziel] += contribution
        
        # Konvergenz prüfen
        diff = sum(abs(neuer_pagerank[s] - pagerank[s]) for s in seiten)
        pagerank = neuer_pagerank
        history.append(pagerank.copy())
        
        if diff < 1e-12:
            print(f"Konvergiert nach {iteration + 1} Iterationen")
            break
    
    # Visualisiere ausgewählte Iterationen
    iterations_to_plot = list(range(min(6, len(history)))) + [len(history) - 1]
    iterations_to_plot = sorted(set(iterations_to_plot))
    
    pdf_files = []
    
    for iter_idx in iterations_to_plot:
        pr_values = history[iter_idx]
        fig = plot_pagerank_step(G, pr_values, seiten, iter_idx, len(history) - 1)
        
        pdf_file = FIG_DIR / f"pagerank_step_{iter_idx:02d}.pdf"
        fig.savefig(pdf_file, dpi=150, bbox_inches='tight')
        pdf_files.append(pdf_file)
        plt.close(fig)
        
        print(f"Gespeichert: {pdf_file}")
        print(f"  Iteration {iter_idx}: {pr_values}")
    
    # Erstelle auch ein Übersichts-PDF mit allen Iterationen
    try:
        create_summary_plot(history, seiten, G)
    except Exception as e:
        print(f"Konnte Übersichts-Plot nicht erstellen: {e}")
    
    # Versuche GIF zu erstellen
    try:
        if Image is not None:
            create_gif_animation(history, seiten, G, pdf_files)
        else:
            print("PIL nicht verfügbar, GIF-Animation übersprungen")
    except Exception as e:
        print(f"Konnte GIF nicht erstellen: {e}")
    
    return history, seiten, G


def create_summary_plot(history, seiten, G):
    """Erstelle einen Überblicks-Plot, der den Konvergenzverlauf zeigt."""
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Plot 1: Konvergenzverläufe
    ax = axes[0, 0]
    iterations = range(len(history))
    for s in seiten:
        values = [h[s] for h in history]
        ax.plot(iterations, values, marker='o', label=f'Seite {s}', linewidth=2)
    ax.set_xlabel('Iteration')
    ax.set_ylabel('PageRank-Wert')
    ax.set_title('Konvergenzverlauf der PageRank-Werte')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Plot 2: Finale PageRank-Verteilung
    ax = axes[0, 1]
    final_pr = history[-1]
    pr_sorted = sorted(final_pr.items(), key=lambda x: x[1], reverse=True)
    sites, values = zip(*pr_sorted)
    colors = plt.cm.YlOrRd(np.linspace(0.3, 0.9, len(sites)))
    ax.bar(sites, values, color=colors)
    ax.set_ylabel('PageRank-Wert')
    ax.set_title('Finale PageRank-Verteilung')
    ax.grid(True, alpha=0.3, axis='y')
    for i, v in enumerate(values):
        ax.text(i, v + 0.005, f'{v:.4f}', ha='center', fontsize=10)
    
    # Plot 3: Netzwerk-Visualisierung mit finalen Werten
    ax = axes[1, 0]
    pos = nx.spring_layout(G, seed=42, k=2, iterations=50)
    final_values = history[-1]
    pr_values = [final_values[s] for s in seiten]
    pr_min, pr_max = min(pr_values), max(pr_values)
    pr_norm = [(v - pr_min) / (pr_max - pr_min + 1e-6) for v in pr_values]
    
    node_sizes = [1000 + 3000 * val for val in pr_norm]
    node_colors = plt.cm.YlOrRd(pr_norm)
    
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, 
                          arrowsize=15, arrowstyle='->', connectionstyle='arc3,rad=0.1',
                          width=2, ax=ax)
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', ax=ax)
    ax.set_title('Finales Netzwerk (mit PageRank)')
    ax.axis('off')
    
    # Plot 4: Konvergenzgeschwindigkeit
    ax = axes[1, 1]
    diffs = [sum(abs(history[i+1][s] - history[i][s]) for s in seiten) 
             for i in range(len(history)-1)]
    ax.semilogy(range(len(diffs)), diffs, marker='o', linewidth=2, color='darkred')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Gesamtänderung (log. Skala)')
    ax.set_title('Konvergenzgeschwindigkeit')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    summary_file = FIG_DIR / "pagerank_summary.pdf"
    fig.savefig(summary_file, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Übersichts-Plot gespeichert: {summary_file}")


def create_gif_animation(history, seiten, G, pdf_files):
    """Erstelle eine GIF-Animation aus den Visualisierungen."""
    
    images = []
    
    # Nutze die bereits erstellten PDFs und konvertiere sie zu Bildern
    # Alternativ: Erstelle PNGs direkt
    png_files = []
    
    iterations_to_plot = list(range(min(6, len(history)))) + [len(history) - 1]
    iterations_to_plot = sorted(set(iterations_to_plot))
    
    for iter_idx in iterations_to_plot:
        pr_values = history[iter_idx]
        fig = plot_pagerank_step(G, pr_values, seiten, iter_idx, len(history) - 1)
        
        png_file = FIG_DIR / f"pagerank_step_{iter_idx:02d}.png"
        fig.savefig(png_file, dpi=100, bbox_inches='tight')
        png_files.append(png_file)
        plt.close(fig)
        
        try:
            img = Image.open(png_file)
            images.append(img)
        except Exception as e:
            print(f"Konnte PNG nicht laden: {e}")
    
    if images:
        gif_file = FIG_DIR / "pagerank_animation.gif"
        images[0].save(
            gif_file,
            save_all=True,
            append_images=images[1:],
            duration=800,
            loop=0
        )
        print(f"GIF-Animation gespeichert: {gif_file}")
        
        # Räume PNGs auf
        for png_file in png_files:
            png_file.unlink()


if __name__ == "__main__":
    print("Visualisiere PageRank-Algorithmus-Schritte...")
    history, seiten, G = run_pagerank_with_visualization()
    
    print("\n=== Finale Ergebnisse ===")
    final_pr = history[-1]
    pr_df = pd.DataFrame({'Seite': seiten, 'PageRank': [final_pr[s] for s in seiten]})
    pr_df = pr_df.sort_values('PageRank', ascending=False).reset_index(drop=True)
    print(pr_df.to_string(index=False))
    print(f"Summe: {sum(final_pr.values()):.6f}")
    print(f"\nAnzahl Iterationen: {len(history) - 1}")
