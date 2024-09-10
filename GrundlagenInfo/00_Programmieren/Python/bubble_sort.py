from copy import deepcopy

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

    caption = f"Schritt {step+1}" if not exchanged else f"Schritt {step+1} (ausgetauscht!)"
    tikz_code += f"\\end{{tikzpicture}}\\caption{{{caption}}}\n"
    
    #filename = f"step_{step}{'_exchanged' if exchanged else ''}.tex"
    filename = f"step_{step+1}{'' if exchanged else ''}.tex"
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
                
    return filenames, arr

# Example array
arr = [5, 3, 8, 20, 2, 10]

# Visualize bubble sort
filenames, arr = bubble_sort_visualize(arr)
print(arr)

# Python code to generate TikZ figures for binary search algorithm and save each step in .tex files

def generate_tikz_binary_search_to_tex(array, target):
    left, right = 0, len(array) - 1
    step = 1

    while left <= right:
        mid = left + (right - left) // 2
        
        # Generate TikZ code for current step
        tikz_code = "\\begin{tikzpicture}\n"        
        # Add array elements to TikZ
        for i, val in enumerate(array):
            if i == mid:
                tikz_code += f"\\node at ({i},0) [rounded corners, minimum width=1cm, minimum height=1cm, draw=blue, thick] {{{val}}};\n"
            else:
                tikz_code += f"\\node[draw=CornflowerBlue, fill=Black!20!White, rounded corners, minimum width=1cm, minimum height=1cm] at ({i}, 0) {{{val}}};\n"
        
        # Add pointers to left, mid, right
        tikz_code += f"\\node[above] at ({left}, 0.5) {{\\lstinline|links|}};\n"
        tikz_code += f"\\node[above] at ({mid}, 0.5) {{\\lstinline|mitte|}};\n"
        tikz_code += f"\\node[above] at ({right}, 0.5) {{\\lstinline|rechts|}};\n"
        
        # Binary search logic
        if array[mid] == target:
            # add checkmark to indicate that number has been found
            tikz_code += f"\\node[below] at ({mid},-.5) {{\emoji{{check-mark-button}}}};\n"
            tikz_code += "\\end{tikzpicture}\n"
        
            # Save to .tex file
            filename = f"binary_search_step_{step}.tex"
            with open(f"{filename}", 'w') as file:
                file.write(tikz_code)
            break
        elif array[mid] < target:
            left = mid + 1
            # save image before curly brace is added
            tikz_code_before = deepcopy(tikz_code) + "\\end{tikzpicture}\n"
            # Save to .tex file
            filename = f"binary_search_step_{step}.tex"
            with open(f"{filename}", 'w') as file:
                file.write(tikz_code_before)
            # add curly brace to highlight part which still needs to be looked at
            tikz_code += f"\\draw[decorate,decoration={{brace,mirror,amplitude=10pt}}] ({left},-.5) -- ({right},-.5) node[midway, below=5pt] {{\emoji{{robot}}}};\n"
        else:
            right = mid - 1
            # save image before curly brace is added
            tikz_code_before = deepcopy(tikz_code) + "\\end{tikzpicture}\n"
            # Save to .tex file
            filename = f"binary_search_step_{step}.tex"
            with open(f"{filename}", 'w') as file:
                file.write(tikz_code_before)

            # add curly brace to highlight part which still needs to be looked at
            tikz_code += f"\\draw[decorate,decoration={{brace,mirror,amplitude=10pt}}] ({left},-.5) -- ({right},-.5) node[midway, below=5pt] {{\emoji{{robot}}}};\n"
        
        tikz_code += "\\end{tikzpicture}\n"
        
        # Save to .tex file
        filename = f"binary_search_step_{step}-next.tex"
        with open(f"{filename}", 'w') as file:
            file.write(tikz_code)
        
        step += 1
        

# Example usage
array = [1, 3, 5, 7, 9, 11, 13, 15]
target = 3

generate_tikz_binary_search_to_tex(array, target)