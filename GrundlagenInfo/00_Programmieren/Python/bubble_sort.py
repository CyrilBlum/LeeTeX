def generate_tikz_figure(data, idx1, idx2, step, exchanged, range=[]):
    tikz_code = "\\begin{tikzpicture}\n"
    
    for i, val in enumerate(data):
        box_color = "LimeGreen" if i in [idx1, idx2] and exchanged else "Lavender" if i in [idx1, idx2] and not exchanged else "CornflowerBlue"
        border_color = "ForestGreen" if i in [idx1, idx2] and exchanged else "OrangeRed" if i in [idx1, idx2] and not exchanged else "Black"
        tikz_code += f"\\node[draw={border_color}, fill={box_color}, rounded corners, minimum width=1cm, minimum height=1cm] at ({i}, 0) {{{val}}};\n"
    
    # Draw arrow and question mark
    if idx1 != idx2:
        symb = "\\emoji{check-mark-button}" if exchanged else "?"
        tikz_code += f"\\path[<->] ({idx1}, .5) edge[bend left=90] node [above]{{{symb}}} ({idx2}, 0.5);\n"
    
    # add curly brace to highlight part which is not sorted yet
    tikz_code += f"\\draw[decorate,decoration={{brace,mirror,amplitude=10pt}}] ({range[0]-.5},-.5) -- ({range[1]+.5},-.5) node[midway, below=5pt] {{\emoji{{robot}}}};\n"

    caption = f"Schritt {step}" if not exchanged else f"Schritt {step} (ausgetauscht!)"
    tikz_code += f"\\end{{tikzpicture}}\\caption{{{caption}}}\n"
    
    #filename = f"step_{step}{'_exchanged' if exchanged else ''}.tex"
    filename = f"step_{step}{'' if exchanged else ''}.tex"
    with open(filename, 'w') as f:
        f.write(tikz_code)
        
    return filename

def bubble_sort_visualize(arr):
    n = len(arr)
    step = 0
    filenames = []
    
    for i in range(n):
        for j in range(0, n-i-1):
            filenames.append(generate_tikz_figure(arr, j, j+1, step, False, range=[0, n-i-1]))
            step += 1
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                filenames.append(generate_tikz_figure(arr, j, j+1, step, True, range=[0, n-i-1]))
                step += 1
                
    return filenames

# Example array
arr = [5, 3, 8, 20, 2, 10]

# Visualize bubble sort
filenames = bubble_sort_visualize(arr)

# Generate LaTeX snippets
with open('bubble_sort_figures.tex', 'w') as f:
    for i, filename in enumerate(filenames):
        f.write(f"\\begin{{figure}}[h!]\n")
        f.write(f"\\centering\n")
        f.write(f"\\input{{{filename}}}\n")
        f.write(f"\\caption{{Step {i}}}\n")
        f.write(f"\\end{{figure}}\n")
        f.write(f"\\clearpage\n")

print("LaTeX snippets generated as 'bubble_sort_figures.tex'.")