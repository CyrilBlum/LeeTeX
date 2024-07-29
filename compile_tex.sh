#!/bin/bash

# Check Bash version
if (( BASH_VERSINFO[0] < 4 )); then
    echo "This script requires Bash version 4.0 or greater."
    exit 1
fi

# Define array of document classes and their toggle positions
declare -a classes=("book" "article" "exam" "beamer")
declare -a toggles=("0" "1" "2" "3")
declare -a class_commands=(
    "\\\\documentclass[a4paper,11pt,svgnames,oneside]{book}"
    "\\\\documentclass[svgnames,hyphens]{article}"
    "\\\\documentclass[11pt,addpoints,svgnames]{exam}"
    "\\\\documentclass[xcolor={table,dvipsnames,svgnames},hyphens]{beamer}"
)

# Declare associative arrays for book topics and their inputs
declare -A book_topics=(
    [Environments]="LaTeX_related/example_file"
    [Zahlendarstellungen und Kodierungen]="GrundlagenInfo/01_TheoretischeInformatik/kapitel01.tex"
    [Induktion und Rekursion]="EF/InduktionUndRekursion/kapitel00.tex EF/InduktionUndRekursion/kapitel01.tex EF/InduktionUndRekursion/kapitel02.tex EF/InduktionUndRekursion/kapitel02.tex EF/InduktionUndRekursion/kapitel03.tex EF/InduktionUndRekursion/kapitel04.tex"
    [Netzwerke]="GrundlagenInfo/07_Netzwerke/kapitel01"
    [Kryptologie]="GrundlagenInfo/07_Netzwerke/Skript_Kryptologie"
    [Datenbanken]="GrundlagenInfo/06_Daten/Kapitel1 GrundlagenInfo/06_Daten/Kapitel2 GrundlagenInfo/06_Daten/Kapitel3 GrundlagenInfo/06_Daten/Kapitel4 GrundlagenInfo/06_Daten/Cheatsheet"
)

# Other document class arrays (for example purposes, actual data needed)
declare -A article_topics=()
declare -A exam_topics=()
declare -A beamer_topics=(
    [Programmieren Prüfung]="GrundlagenInfo/00_Programmieren/Examples_Exam"
    [Programmieren Kapitel 01 Einführung]="GrundlagenInfo/00_Programmieren/Kapitel01Intro"
    [Programmieren Kapitel 02a Definitionen]="GrundlagenInfo/00_Programmieren/Kapitel02aDefinitionen"
    [Programmieren Kapitel 02b Animationen]="GrundlagenInfo/00_Programmieren/Kapitel02bAnimationen"
    [Programmieren Kapitel 02c Animationen]="GrundlagenInfo/00_Programmieren/Kapitel02bAnimationen"
)

# Directory where your LaTeX files are stored
root_dir=$(pwd)
pwd
ls -la
latex_dir="${root_dir}/PDFs/"
server_dir="/var/www/in-form-atik.ch/public_html/pdfs/"

# remove all formerly compiled files
cd $latex_dir
rm -f *.bcf *.ist *.log *.aux *.xml *.idx *.glo *.toc *.gz *.nav *.snm *vrb *.pdf
cd $root_dir

# Loop over each document class
for i in "${!classes[@]}"; do
    class_variable="${classes[$i]}_topics"  # Dynamically get the name of the array 
    declare -n current_class_topics=$class_variable  # Use nameref to refer to the correct associative array

    # Check if the current class has any topics defined
    if [ ${#current_class_topics[@]} -eq 0 ]; then
        echo "No topics defined for ${classes[$i]}, skipping..."
        continue
    fi

    # loop each topic
    for topic in "${!current_class_topics[@]}"; do
        input_files=(${current_class_topics[$topic]})  # Split the string into an array

        # Prepare the file name
        output_file="${root_dir}/output_${classes[$i]}_${topic// /_}.tex"
        cp ${root_dir}/main.tex $output_file
	
	    # Replace the document class line
    	sed -i "s/\\\\documentclass.*{.*}/${class_commands[$i]}/" "$output_file"
    	
   	    # Replace the document class toggle line
    	sed -i "s/\\\\def\\\\documentToggle{[0-9]}/\\\\def\\\\documentToggle{${toggles[$i]}}/" "$output_file"
    	
	    # replace the topic line
        sed -i "s/\\\\newcommand{\\\\thetopic}{.*}/\\\\newcommand{\\\\thetopic}{${topic}}/" "$output_file"

        # Uncomment the necessary input lines
        for input_path in "${input_files[@]}"; do
		    sed -i "s|[[:space:]]*%[[:space:]]*\\\\input{${input_path}}|\\\\input{${input_path}}|" "$output_file"
        done

        # Compile the LaTeX document
        lualatex -synctex=1 -interaction=nonstopmode -output-directory="$latex_dir" "$output_file"

        # second run, to compile also TOC and other things
        lualatex -synctex=1 -interaction=nonstopmode -output-directory="$latex_dir" "$output_file"

	    # copy final file to server
	    # cp ${latex_dir}output_${classes[$i]}_${topic// /_}.pdf ${server_dir}output_${classes[$i]}_${topic// /_}.pdf 

	
        # Clean up if necessary
        rm "$output_file"  # Uncomment to delete the intermediate .tex files
    done
done

# remove all aux files
cd $latex_dir
rm -f *.bcf *.ist *.log *.aux *.xml *.idx *.glo *.toc *.gz *.nav *.snm *vrb
cd $root_dir

echo "Compilation of all document types complete."