def generate_tikz_figure(data, idx1, idx2, step, exchanged):
    tikz_code = "\\begin{tikzpicture}\n"
    
    for i, val in enumerate(data):
        box_color = "white" if i in [idx1, idx2] else "#99ccff"
        border_color = "red" if i in [idx1, idx2] else "black"
        tikz_code += f"\\node[draw={border_color}, fill={box_color}, rounded corners, minimum width=1cm, minimum height=1cm] at ({i}, 0) {{{val}}};\n"
        
    # Draw arrow and question mark
    if idx1 != idx2:
        tikz_code += f"\\draw[->, thick] ({idx1}, 0.5) -- ({idx2}, 0.5) node[midway, above] {{?}};\n"
    
    tikz_code += "\\end{tikzpicture}\n"
    
    filename = f"step_{step}{'_exchanged' if exchanged else ''}.tex"
    with open(filename, 'w') as f:
        f.write(tikz_code)
        
    return filename

def bubble_sort_visualize(arr):
    n = len(arr)
    step = 0
    filenames = []
    
    for i in range(n):
        for j in range(0, n-i-1):
            filenames.append(generate_tikz_figure(arr, j, j+1, step, False))
            step += 1
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                filenames.append(generate_tikz_figure(arr, j, j+1, step, True))
                step += 1
                
    return filenames

# Example array
arr = [5, 3, 8, 4, 2]

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