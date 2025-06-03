#!/bin/bash
# At the top of compile_tex.sh
LEE_TEX_SSH_PASSWORD="$1"

echo "Length: ${#LEE_TEX_SSH_PASSWORD}"

# This script is POSIX-compatible and works on macOS (Bash 3.x), Ubuntu, and Zsh.

# Define array of document classes and their toggle positions

classes=("book" "book" "article" "exam")
toggles=("0" "0" "1" "2") # documentclass toggles

# classes=("book" "book" "article" "exam" "beamer")
# toggles=("0" "0" "1" "2" "3") # documentclass toggles

class_commands=(
    "\\\\documentclass[a4paper,11pt,svgnames,oneside]{book}"
    "\\\\documentclass[a4paper,11pt,svgnames,exerciseonly,oneside]{book}"
    "\\\\documentclass[svgnames,hyphens]{article}"
    "\\\\documentclass[11pt,addpoints,svgnames]{exam}"
    # "\\\\documentclass[xcolor={table,dvipsnames,svgnames},hyphens]{beamer}"
)

# Topics and their input files for each document class (as flat arrays: topic:path)
book_topics=(
    # OInf topics
    "Programmieren:GrundlagenInfo/00_Programmieren/Skript/Skript.tex"
    "Zahlendarstellungen_und_Kodierungen:GrundlagenInfo/01_TheoretischeInformatik/Skript/Skript.tex"
    "Randomisierte_Algorithmen:GrundlagenInfo/01_TheoretischeInformatik/Randomisierte_Algorithmen/Skript/Skript.tex"
    "Kryptologie:GrundlagenInfo/03_Kryptologie/Skript/Skript.tex"
    "Kompression:GrundlagenInfo/04_Kompression/Skript.tex"
    "Datenintegrität:GrundlagenInfo/05_DatenIntegritaet/Skript/Skript"
    "Datenbanken:GrundlagenInfo/06_Datenbanken/Skript/Skript.tex"
    "Netzwerke:GrundlagenInfo/07_Netzwerke/Skript.tex"
    "Tabellenkalkulation:GrundlagenInfo/09_Tabellenkalkulation/skript_tabellenkalkulation.tex"
    "Aus_Daten_Lernen:GrundlagenInfo/10_AusDatenLernen/Skript/Skript.tex"
    # Cyril Geography topics
    "Stadtgeografie:Geografie/Stadtgeografie/Skript/Skript.tex"
    "Geomorphologie:Geografie/Geomorphologie/Skript/Skript.tex"
    # Thomas EF topics
    # "Endliche_Automaten:EF/EndlicheAutomaten/skript_EA.tex"
    # "Induktion_und_Rekursion:EF/InduktionUndRekursion/skript_induktion_rekursion.tex"
    # "Kolmogorov-Komplexitaet:EF/Kolmogorov/skript_kolmogorov.tex"
)

article_topics=(
    "Unterrichtsvorbereitung:Private/PHBern/3 BPA/Unterrichtsvorbereitung.tex"
)

exam_topics=(
    "Stadtgeografie_NHP:Geografie/Stadtgeografie/Prüfungen/Stadtgeografie_NHP.tex"
)

beamer_topics=(
    "K01Intro:GrundlagenInfo/00_Programmieren/Slides/K01Intro"
    "K01aZeichenketten:GrundlagenInfo/00_Programmieren/Slides/K01aZeichenketten"
    "K02aDefinitionen:GrundlagenInfo/00_Programmieren/Slides/K02aDefinitionen"
    "K02bAnimationen:GrundlagenInfo/00_Programmieren/Slides/K02bAnimationen"
    "K03aParameter:GrundlagenInfo/00_Programmieren/Slides/K03aParameter"
    "K03bVariablen:GrundlagenInfo/00_Programmieren/Slides/K03bVariablen"
    "K03cZeitTabellen:GrundlagenInfo/00_Programmieren/Slides/K03cZeitTabellen"
    "K03dInput:GrundlagenInfo/00_Programmieren/Slides/K03dInput"
    "K04aIfElifElse:GrundlagenInfo/00_Programmieren/Slides/K04aIfElifElse"
    "K04bLogischeOperatoren:GrundlagenInfo/00_Programmieren/Slides/K04bLogischeOperatoren"
    "K04cNegation:GrundlagenInfo/00_Programmieren/Slides/K04cNegation"
    "K04dBreakWhile:GrundlagenInfo/00_Programmieren/Slides/K04dBreakWhile"
    "K04zModulo:GrundlagenInfo/00_Programmieren/Slides/K04zModulo"
    "K05aListen:GrundlagenInfo/00_Programmieren/Slides/K05aListen"
    "K05bBubbleSort:GrundlagenInfo/00_Programmieren/Slides/K05bBubbleSort"
    "K05cBinarySearch:GrundlagenInfo/00_Programmieren/Slides/K05cBinarySearch"
    "K05dListenTeil2:GrundlagenInfo/00_Programmieren/Slides/K05dListenTeil2"
    "K07aFunktionenEinzelne:GrundlagenInfo/00_Programmieren/Slides/K07aFunktionenEinzelne"
    "K07bFunktionenMehrere:GrundlagenInfo/00_Programmieren/Slides/K07bFunktionenMehrere"
    "TurtleGrafik:GrundlagenInfo/00_Programmieren/TurtleGrafik"
    "Zahlensysteme_L01:GrundlagenInfo/01_TheoretischeInformatik/Slides/Zahlensysteme_L01"
    "Zahlensysteme_L02:GrundlagenInfo/01_TheoretischeInformatik/Slides/Zahlensysteme_L02"
    "Zahlensysteme_L03:GrundlagenInfo/01_TheoretischeInformatik/Slides/Zahlensysteme_L03"
    "Zahlensysteme_L04:GrundlagenInfo/01_TheoretischeInformatik/Slides/Zahlensysteme_L04"
    "Zahlensysteme_L05:GrundlagenInfo/01_TheoretischeInformatik/Slides/Zahlensysteme_L05"
    "Graphen_L01:GrundlagenInfo/02_Graphen/Graphen_L01"
    "Graphen_L02:GrundlagenInfo/02_Graphen/Graphen_L02"
    "Graphen_L03:GrundlagenInfo/02_Graphen/Graphen_L03"
    "AbstraktionDurchGraphen_Kapitel01:GrundlagenInfo/02_Graphen/AbstraktionDurchGraphen/Slides_Kapitel01"
    "AbstraktionDurchGraphen_Kapitel02:GrundlagenInfo/02_Graphen/AbstraktionDurchGraphen/Slides_Kapitel02"
    "Kryptologie_L01:GrundlagenInfo/03_Kryptologie/Slides/Kryptologie_L01"
    "Kryptologie_L01prog:GrundlagenInfo/03_Kryptologie/Slides/Kryptologie_L01prog"
    "L02a_Kryptoanalyse_Caesar:GrundlagenInfo/03_Kryptologie/Slides/L02a_Kryptoanalyse_Caesar"
    "L02b_Kryptoanalyse_Monoalph:GrundlagenInfo/03_Kryptologie/Slides/L02b_Kryptoanalyse_Monoalph"
    "L02c_Kryptoanalyse_Vigenere:GrundlagenInfo/03_Kryptologie/Slides/L02c_Kryptoanalyse_Vigenere"
    "L02d_Kryptoanalyse_Vigenere_Friedman:GrundlagenInfo/03_Kryptologie/Slides/L02d_Kryptoanalyse_Vigenere_Friedman"
    "L02e_Kryptoanalyse_Vigenere_Kasiski:GrundlagenInfo/03_Kryptologie/Slides/L02e_Kryptoanalyse_Vigenere_Kasiski"
    "Kryptologie_L02:GrundlagenInfo/03_Kryptologie/Slides/Kryptologie_L02"
    "Appendix:GrundlagenInfo/03_Kryptologie/Slides/Appendix"
    "Kompression_L01:GrundlagenInfo/04_Kompression/Kompression_L01"
    "Kompression_L02:GrundlagenInfo/04_Kompression/Kompression_L02"
    "01_Intro:GrundlagenInfo/05_DatenIntegritaet/Slides/01_Intro"
    "02_Fehlererkennung:GrundlagenInfo/05_DatenIntegritaet/Slides/02_Fehlererkennung"
    "03_Fehlerkorrektur:GrundlagenInfo/05_DatenIntegritaet/Slides/03_Fehlerkorrektur"
    "04_Kartentrick:GrundlagenInfo/05_DatenIntegritaet/Slides/04_Kartentrick"
    "05_RAID:GrundlagenInfo/05_DatenIntegritaet/Slides/05_RAID"
    "01_Slides_Intro:GrundlagenInfo/05_DatenIntegritaet/Slides/01_Slides_Intro"
    "02_Slides_SELECT:GrundlagenInfo/06_Datenbanken/Slides/02_Slides_SELECT"
    "02b_Slides_Subqueries:GrundlagenInfo/06_Datenbanken/Slides/02b_Slides_Subqueries"
    "03_Slides_JOIN:GrundlagenInfo/06_Datenbanken/Slides/03_Slides_JOIN"
    "04_Slides_DML:GrundlagenInfo/06_Datenbanken/Slides/04_Slides_DML"
    "05_Slides_Game:GrundlagenInfo/06_Datenbanken/Slides/05_Slides_Game"
    "Netzwerke_L01:GrundlagenInfo/07_Netzwerke/Netzwerke_L01"
    "correlation_causation:GrundlagenInfo/10_AusDatenLernen/Slides/correlation_causation.tex"
    "linear_regression:GrundlagenInfo/10_AusDatenLernen/Slides/linear_regression.tex"
    "markov_chains:GrundlagenInfo/10_AusDatenLernen/Slides/markov_chains.tex"
    "markov_appendix:GrundlagenInfo/10_AusDatenLernen/Slides/markov_appendix.tex"
    "complexity:EF/Complexity/complexity.tex"
    "Presentation_MINT_Tag:Various/MINT_Tag/Presentation_MINT_Tag.tex"
)

root_dir=$(pwd)
latex_dir="${root_dir}/PDFs/"

# Remove all formerly compiled files
if [ -d "$latex_dir" ]; then
    cd "$latex_dir"
    rm -f *.bcf *.ist *.log *.aux *.xml *.idx *.glo *.toc *.gz *.nav *.snm *vrb *.pdf *.bbl *.blg *.lot *.lof *.gls *glg
    cd "$root_dir"
fi

# Detect OS for sed in-place flag
if [[ "$OSTYPE" == "darwin"* ]]; then
    SED_INPLACE=(-i '')
else
    SED_INPLACE=(-i)
fi

# Loop over each document class
for i in "${!classes[@]}"; do
    class="${classes[$i]}"
    toggle="${toggles[$i]}"
    class_command="${class_commands[$i]}"
    topics_var="${class}_topics[@]"
    topics=("${!topics_var}")

    if [ ${#topics[@]} -eq 0 ]; then
        echo "No topics defined for $class, skipping..."
        continue
    fi

    for entry in "${topics[@]}"; do
        topic="${entry%%:*}"
        input_path="${entry#*:}"

        # Determine output directory and file names, distinguishing between book variants
        if [ "$class" = "book" ]; then
            # Check if this is the exerciseonly variant
            if echo "$class_command" | grep -q "exerciseonly"; then
                book_variant="exerciseonly"
                latex_dir="${root_dir}/PDFs/${topic}/${class}_${book_variant}/"
                output_file="${root_dir}/output_${class}_${book_variant}_${topic// /_}.tex"
            else
                book_variant="solutions"
                latex_dir="${root_dir}/PDFs/${topic}/${class}_${book_variant}/"
                output_file="${root_dir}/output_${class}_${book_variant}_${topic// /_}.tex"
            fi
        elif [ "$class" != "book" ]; then
            # put files in slides folder (not structured by topic)
            latex_dir="${root_dir}/PDFs/${class}/${topic}/"
            output_file="${root_dir}/output_${class}_${topic// /_}.tex"
        else
            latex_dir="${root_dir}/PDFs/${topic}/${class}/"
            output_file="${root_dir}/output_${class}_${topic// /_}.tex"
        fi
        mkdir -p "$latex_dir"

        # Print current values for debugging
        echo "Processing entry: $entry"
        echo "  topic: $topic"
        echo "  input_path: $input_path"
        echo "  output_file: $output_file"
        echo "  output_dir: $latex_dir"

        cp "${root_dir}/main.tex" "$output_file"

        # Replace the document class line
        sed "${SED_INPLACE[@]}" "s/\\\\\documentclass.*{.*}/$class_command/" "$output_file"
        # Replace the document class toggle line
        sed "${SED_INPLACE[@]}" "s/\\\\\def\\\\\documentToggle{[0-9]}/\\\\def\\\\documentToggle{$toggle}/" "$output_file"
        # Replace the topic line (if present)
        sed "${SED_INPLACE[@]}" "s/\\\\newcommand{\\\\thetopic}{.*}/\\\\newcommand{\\\\thetopic}{$topic}/" "$output_file"
        # Uncomment the necessary input line
        sed "${SED_INPLACE[@]}" "s|[[:space:]]*%*[[:space:]]*\\\\input{$input_path}|\\\\input{$input_path}|" "$output_file"

        # Copy cyril.tex and set topic/subject
        cyril_src="${root_dir}/Setups/cyril.tex"
        if [ "$class" = "book" ]; then
            cyril_out="${root_dir}/Setups/cyril_${class}_${book_variant}_${topic// /_}.tex"
        else
            cyril_out="${root_dir}/Setups/cyril_${class}_${topic// /_}.tex"
        fi
        cp "$cyril_src" "$cyril_out"
        echo "  Using cyril.tex: $cyril_out"

        # Comment out all "thetopic" lines
        sed "${SED_INPLACE[@]}" "/\\\\newcommand{\\\\thetopic}/s/^/%/" "$cyril_out"
        # Uncomment the selected topic line
        sed "${SED_INPLACE[@]}" "/\\\\newcommand{\\\\thetopic}{${topic//_/ }}/s/^%*[[:space:]]*//" "$cyril_out"

        # Comment out all "thesubject" lines
        sed "${SED_INPLACE[@]}" "/\\\\newcommand{\\\\thesubject}/s/^/%/" "$cyril_out"
        # Set the correct \thesubject line: uncomment Geografie if topic matches, else Informatik
        if echo "$topic" | grep -Eq "Stadtgeografie|Geomorphologie|Globalisierung|Geografie"; then
            # Uncomment Informatik line
            sed "${SED_INPLACE[@]}" "/\\\\newcommand{\\\\thesubject}{Geografie}/s/^%*[[:space:]]*//" "$cyril_out"
        else
            # Uncomment Informatik line
            sed "${SED_INPLACE[@]}" "/\\\\newcommand{\\\\thesubject}{Informatik}/s/^%*[[:space:]]*//" "$cyril_out"
        fi

        # Use the custom cyril.tex in the main file copy
        if [ "$class" = "book" ]; then
            sed "${SED_INPLACE[@]}" "s|\\input{Setups/cyril.tex}|\\input{Setups/cyril_${class}_${book_variant}_${topic// /_}.tex}|" "$output_file"
        else
            sed "${SED_INPLACE[@]}" "s|\\input{Setups/cyril.tex}|\\input{Setups/cyril_${class}_${topic// /_}.tex}|" "$output_file"
        fi

        if [ "$class" = "book" ]; then
            # Compile for 'book': lualatex -> biber -> makeglossaries -> lualatex -> lualatex
            echo "  step 1: lualatex"
            lualatex -synctex=1 -interaction=nonstopmode -output-directory="$latex_dir" "$output_file" | grep -E "^(!|l\.)" || true

            echo "  step 2: biber"
            biber --input-directory="$latex_dir" --output-directory="$latex_dir" "$(basename "$output_file" .tex)"

            echo "  step 3: makeglossaries"
            makeglossaries -d "$latex_dir" "$(basename "$output_file" .tex)" || true

            echo "  step 4: lualatex"
            lualatex -synctex=1 -interaction=nonstopmode -output-directory="$latex_dir" "$output_file" | grep -E "^(!|l\.)|Warning" || true

            echo "  step 5: lualatex"
            lualatex -synctex=1 -interaction=nonstopmode -output-directory="$latex_dir" "$output_file" | grep -E "^(!|l\.)|Warning" || true
        else
            # Double pass for other classes, show only warnings/errors
            echo "  step 1: lualatex"
            lualatex -synctex=1 -interaction=nonstopmode -output-directory="$latex_dir" "$output_file" | grep -E "^(!|l\.)|Warning" || true
            echo "  step 2: lualatex"
            lualatex -synctex=1 -interaction=nonstopmode -output-directory="$latex_dir" "$output_file" | grep -E "^(!|l\.)|Warning" || true
        fi

        log_file="${latex_dir}$(basename "$output_file" .tex).log"
        if grep -q '^!' "$log_file"; then
            echo "LaTeX error detected. Aborting."
            exit 1
        fi

        # Clean up intermediate .tex file
        rm "$output_file"
        rm "$cyril_out"

        # Remove all aux files (but keep log files and PDFs)
        if [ -d "$latex_dir" ]; then
            cd "$latex_dir"
            rm -f *.bcf *.ist *.aux *.xml *.idx *.glo *.toc *.gz *.nav *.snm *vrb *.bbl *.blg *.lot *.lof *.gls *glg
            cd "$root_dir"
        fi
    done
done

# Copy all files and folders from PDFs to Cyril's Synology NAS
if [ "$OSTYPE" != "darwin"* ]; then
    # Use sshpass to provide the password non-interactively (not recommended for security reasons)
    sshpass -p "${LEE_TEX_SSH_PASSWORD}" rsync -av --chmod=ugo=rwX -e ssh "${root_dir}/PDFs/" leetex@51.154.36.16::LeeTeX/PDFs
fi

echo "Compilation of all document types complete."
