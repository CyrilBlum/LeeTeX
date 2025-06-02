#!/bin/bash

# This script is POSIX-compatible and works on macOS (Bash 3.x), Ubuntu, and Zsh.

# Define array of document classes and their toggle positions
classes=("book" "article" "exam" "beamer")
toggles=("0" "1" "2" "3")
class_commands=(
    "\\\\documentclass[a4paper,11pt,svgnames,oneside]{book}"
    "\\\\documentclass[svgnames,hyphens]{article}"
    "\\\\documentclass[11pt,addpoints,svgnames]{exam}"
    "\\\\documentclass[xcolor={table,dvipsnames,svgnames},hyphens]{beamer}"
)

# Topics and their input files for each document class (as flat arrays: topic:path)
book_topics=(
  "Programmieren:GrundlagenInfo/00_Programmieren/Skript/Skript.tex"
  "Zahlendarstellungen_und_Kodierungen:GrundlagenInfo/01_TheoretischeInformatik/Skript/Skript.tex"
#   "Randomisierte_Algorithmen:GrundlagenInfo/01_TheoretischeInformatik/Randomisierte_Algorithmen/Skript/Skript.tex"
#   "Kryptologie:GrundlagenInfo/03_Kryptologie/Skript/Skript.tex"
#   "Kompression:GrundlagenInfo/04_Kompression/Skript.tex"
#   "Datenintegritaet:GrundlagenInfo/05_DatenIntegritaet/Skript/Skript"
#   "Datenbanken:GrundlagenInfo/06_Datenbanken/Skript/Skript.tex"
#   "Datenbanken_Ag:GrundlagenInfo/06_Datenbanken/skript_DB_Ag.tex"
#   "Netzwerke:GrundlagenInfo/07_Netzwerke/Skript.tex"
#   "Tabellenkalkulation:GrundlagenInfo/09_Tabellenkalkulation/skript_tabellenkalkulation.tex"
#   "Aus_Daten_lernen:GrundlagenInfo/10_AusDatenLernen/Skript/Skript.tex"
#   "Endliche_Automaten:EF/EndlicheAutomaten/skript_EA.tex"
#   "Induktion_und_Rekursion:EF/InduktionUndRekursion/skript_induktion_rekursion.tex"
#   "Kolmogorov-Komplexitaet:EF/Kolmogorov/skript_kolmogorov.tex"
#   "Stadtgeografie:Geografie/Stadtgeografie/Skript/Skript.tex"
#   "Geomorphologie:Geografie/Geomorphologie/Skript/Skript.tex"
)

article_topics=(
  "Unterrichtsvorbereitung:Private/PHBern/3 BPA/Unterrichtsvorbereitung.tex"
)

exam_topics=(
  "Stadtgeografie_NHP:Geografie/Stadtgeografie/Prüfungen/Stadtgeografie_NHP.tex"
)

beamer_topics=(
  "Markov_Ketten:GrundlagenInfo/10_AusDatenLernen/Slides/markov_chains.tex"
  "Lineare_Regression:GrundlagenInfo/10_AusDatenLernen/Slides/linear_regression.tex"
  "Correlation_Causation:GrundlagenInfo/10_AusDatenLernen/Slides/correlation_causation.tex"
)

root_dir=$(pwd)
latex_dir="${root_dir}/PDFs/"
server_dir="/var/www/in-form-atik.ch/public_html/pdfs/"

# Remove all formerly compiled files
if [ -d "$latex_dir" ]; then
  cd "$latex_dir"
  rm -f *.bcf *.ist *.log *.aux *.xml *.idx *.glo *.toc *.gz *.nav *.snm *vrb *.pdf *.bbl *.blg
  cd "$root_dir"
fi

# Loop over each document class
for i in "${!classes[@]}"; do
  class="${classes[$i]}"
  toggle="${toggles[$i]}"
  class_command="${class_commands[$i]}"
  topics_var="${class}_topics[@]"
  topics=( "${!topics_var}" )

  if [ ${#topics[@]} -eq 0 ]; then
    echo "No topics defined for $class, skipping..."
    continue
  fi

  for entry in "${topics[@]}"; do
    topic="${entry%%:*}"
    input_path="${entry#*:}"
    output_file="${root_dir}/output_${class}_${topic// /_}.tex"

    # Print current values for debugging
    echo "Processing entry: $entry"
    echo "  topic: $topics"
    echo "  input_path: $input_path"
    echo "  output_file: $output_file"

    cp "${root_dir}/main.tex" "$output_file"

    # Replace the document class line
    sed -i '' "s/\\\\\documentclass.*{.*}/$class_command/" "$output_file"
    # Replace the document class toggle line
    sed -i '' "s/\\\\\def\\\\\documentToggle{[0-9]}/\\\\def\\\\documentToggle{$toggle}/" "$output_file"
    # Replace the topic line (if present)
    sed -i '' "s/\\\\newcommand{\\\\thetopic}{.*}/\\\\newcommand{\\\\thetopic}{$topic}/" "$output_file"
    # Uncomment the necessary input line
    sed -i '' "s|[[:space:]]*%[[:space:]]*\\\\input{$input_path}|\\\\input{$input_path}|" "$output_file"

    # Copy cyril.tex and set topic/subject
    cyril_src="${root_dir}/Setups/cyril.tex"
    cyril_out="${root_dir}/Setups/cyril_${class}_${topic// /_}.tex"
    cp "$cyril_src" "$cyril_out"

    # Uncomment the correct \thetopic line (matching the topic)
    sed -i '' "/^% \\\\newcommand{\\\\thetopic}{.*$topic.*}/s/^% //" "$cyril_out"
    # Comment out all other \thetopic lines
    sed -i '' "/^\\\\newcommand{\\\\thetopic}{.*}/{
      /$topic/!s/^/% /
    }" "$cyril_out"

    # Uncomment and set the correct \thesubject line
    if echo "$topic" | grep -Eq "Stadtgeografie|Geomorphologie|Globalisierung|Geografie"; then
      sed -i '' "/^% \\\\newcommand{\\\\thesubject}{Geografie}/s/^% //" "$cyril_out"
      sed -i '' "/^\\\\newcommand{\\\\thesubject}{Informatik}/s/^/% /" "$cyril_out"
    else
      sed -i '' "/^% \\\\newcommand{\\\\thesubject}{Informatik}/s/^% //" "$cyril_out"
      sed -i '' "/^\\\\newcommand{\\\\thesubject}{Geografie}/s/^/% /" "$cyril_out"
    fi

    # Use the custom cyril.tex in the main file copy
    sed -i '' "s|\\\\input{Setups/cyril.tex}|\\\\input{Setups/cyril_${class}_${topic// /_}.tex}|" "$output_file"

    # if [ "$class" = "book" ]; then
    #   # Compile for 'book': lualatex -> biber -> makeglossaries -> lualatex -> lualatex
    #   lualatex -synctex=1 -interaction=nonstopmode -output-directory="$latex_dir" "$output_file"
    #   biber "${latex_dir}/$(basename "$output_file" .tex)"
    #   makeglossaries "$(basename "$output_file" .tex)"
    #   lualatex -synctex=1 -interaction=nonstopmode -output-directory="$latex_dir" "$output_file"
    #   lualatex -synctex=1 -interaction=nonstopmode -output-directory="$latex_dir" "$output_file"
    # else
    #   # Single pass for other classes
    #   lualatex -synctex=1 -interaction=nonstopmode -output-directory="$latex_dir" "$output_file"
    # fi

    # Clean up intermediate .tex file
    rm "$output_file"
    rm "$cyril_out"
  done
done

# Remove all aux files
if [ -d "$latex_dir" ]; then
  cd "$latex_dir"
  rm -f *.bcf *.ist *.aux *.xml *.idx *.glo *.toc *.gz *.nav *.snm *vrb *.bbl *.blg
  cd "$root_dir"
fi

echo "Compilation of all document types complete."