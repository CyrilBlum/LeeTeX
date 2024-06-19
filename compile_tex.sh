#!/bin/bash

# Define array of document classes and their toggle positions
declare -a classes=("book" "article" "exam" "beamer")
declare -a toggles=("0" "1" "2" "3")
declare -a class_commands=(
    "\\documentclass[a4paper,11pt,svgnames,oneside]{book}"
    "\\documentclass[svgnames,hyphens]{article}"
    "\\documentclass[11pt,addpoints,svgnames]{exam}"
    "\\documentclass[xcolor={table,dvipsnames,svgnames},hyphens]{beamer}"
)

# Declare associative arrays for book topics and their inputs
declare -A book_topics=(
    [Induktion und Rekursion]="EF/InduktionUndRekursion/kapitel00.tex EF/InduktionUndRekursion/kapitel01.tex"
    [Netzwerke]="GrundlagenInfo/07_Netzwerke/kapitel01"
    [Datenbanken]="GrundlagenInfo/06_Daten/Kapitel1 GrundlagenInfo/06_Daten/Kapitel2 GrundlagenInfo/06_Daten/Kapitel3 GrundlagenInfo/06_Daten/Kapitel4"
)

# Other document class arrays (for example purposes, actual data needed)
declare -A article_topics=()
declare -A exam_topics=()
declare -A beamer_topics=()

# Directory where your LaTeX files are stored
latex_dir="/root/GitHub/PDFs/"
latex_dir_in="/root/GitHub/LeeTeX/"

# Loop over each document class
for i in "${!classes[@]}"; do
    class_variable="${classes[$i]}_topics"  # Dynamically get the name of the array 
    declare -n current_class_topics=$class_variable  # Use nameref to refer to the correct associative array

    # Check if the current class has any topics defined
    if [ ${#current_class_topics[@]} -eq 0 ]; then
        echo "No topics defined for ${classes[$i]}, skipping..."
        continue
    fi


    for topic in "${!current_class_topics[@]}"; do
        input_files=(${current_class_topics[$topic]})  # Split the string into an array

        # Prepare the file name
        output_file="${latex_dir_in}output_${classes[$i]}_${topic// /_}.tex"
        cp ${latex_dir_in}main.tex $output_file

        # Replace the document class line and the topic
        sed -i "s/\\\\documentclass.*{.*}/${class_commands[$i]}/" "$output_file"
        sed -i "s/\\\\newcommand{\\\\thetopic}{.*}/\\\\newcommand{\\\\thetopic}{${topic}}/" "$output_file"

        # Uncomment the necessary input lines
        for input_path in "${input_files[@]}"; do
           	echo  sed -i "s|% \\\\input{${input_path}}|\\\\input{${input_path}}|" "$output_file"
		sed -i "s|% \\\\input{${input_path}}|\\\\input{${input_path}}|" "$output_file"
        done

        # Compile the LaTeX document
        lualatex -output-directory="$latex_dir" "$output_file"
 
        # Clean up if necessary
        # rm "$output_file"  # Uncomment to delete the intermediate .tex files
    done
done

echo "Compilation of all document types complete."
