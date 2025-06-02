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
# Use updated paths matching the current repo structure

declare -A book_topics=(
    [Programmieren]="GrundlagenInfo/00_Programmieren/Skript/Skript.tex"
    [Zahlendarstellungen_und_Kodierungen]="GrundlagenInfo/01_TheoretischeInformatik/Skript/Skript.tex"
    [Randomisierte_Algorithmen]="GrundlagenInfo/01_TheoretischeInformatik/Randomisierte_Algorithmen/Skript/Skript.tex"
    [Kryptologie]="GrundlagenInfo/03_Kryptologie/Skript/Skript.tex"
    [Kompression]="GrundlagenInfo/04_Kompression/Skript.tex"
    [Datenintegritaet]="GrundlagenInfo/05_DatenIntegritaet/Skript/Skript"
    [Datenbanken]="GrundlagenInfo/06_Datenbanken/Skript/Skript.tex"
    [Datenbanken_Ag]="GrundlagenInfo/06_Datenbanken/skript_DB_Ag.tex"
    [Netzwerke]="GrundlagenInfo/07_Netzwerke/Skript.tex"
    [Tabellenkalkulation]="GrundlagenInfo/09_Tabellenkalkulation/skript_tabellenkalkulation.tex"
    [Aus_Daten_lernen]="GrundlagenInfo/10_AusDatenLernen/Skript/Skript.tex"
    [Endliche_Automaten]="EF/EndlicheAutomaten/skript_EA.tex"
    [Induktion_und_Rekursion]="EF/InduktionUndRekursion/skript_induktion_rekursion.tex"
    [Kolmogorov-Komplexitaet]="EF/Kolmogorov/skript_kolmogorov.tex"
    [Stadtgeografie]="Geografie/Stadtgeografie/Skript/Skript.tex"
    [Geomorphologie]="Geografie/Geomorphologie/Skript/Skript.tex"
)

# ARTICLE: e.g. Unterrichtsvorbereitung, Handouts, etc.
declare -A article_topics=(
    [Unterrichtsvorbereitung]="Private/PHBern/3 BPA/Unterrichtsvorbereitung.tex"
)

# EXAM: add real exam files if needed
declare -A exam_topics=(
    [Stadtgeografie_NHP]="Geografie/Stadtgeografie/Prüfungen/Stadtgeografie_NHP.tex"
)

# BEAMER: Slides for each topic
declare -A beamer_topics=(
    [Markov_Ketten]="GrundlagenInfo/10_AusDatenLernen/Slides/markov_chains.tex"
    [Lineare_Regression]="GrundlagenInfo/10_AusDatenLernen/Slides/linear_regression.tex"
    [Correlation_Causation]="GrundlagenInfo/10_AusDatenLernen/Slides/correlation_causation.tex"
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