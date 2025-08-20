#!/bin/bash
# At the top of compile_tex.sh
LEE_TEX_SSH_PASSWORD="$1"
CHANGED_FILES_CSV="$2"

# Parse changed files into an array (if provided)
IFS=',' read -r -a CHANGED_FILES <<<"$CHANGED_FILES_CSV"

# Helper to check if PDF exists on remote server using sshpass and ls -l
remote_pdf_exists() {
    local remote_pdf_path="$1"
    # Only check on Linux (not macOS)
    if [[ "$OSTYPE" == *darwin* ]]; then
        echo "::notice::Skipping remote PDF check on macOS."
        return 1 # Always "not found" on macOS
    fi
    # Convert remote_pdf_path (PDFs/...) to absolute path on server
    local abs_remote_path="/volume1/LeeTeX/$remote_pdf_path"
    echo "::group::Checking remote PDF existence"
    echo "::notice:: abs_remote_path: $abs_remote_path"
    ssh_output=$(sshpass -p "$LEE_TEX_SSH_PASSWORD" ssh -p 50037 -o StrictHostKeyChecking=no leetex@51.154.36.16 "ls -l '$abs_remote_path'")
    ssh_exit=$?
    echo "::notice:: ssh exit code: $ssh_exit"
    echo "::notice:: ssh output:"
    echo "$ssh_output"
    if [ $ssh_exit -eq 0 ]; then
        echo "::notice:: File $remote_pdf_path exists on server (ssh)."
        echo "::endgroup::"
        return 0
    else
        echo "::notice:: File $remote_pdf_path does not exist on server (ssh)."
        echo "::endgroup::"
        return 1
    fi
}

# Function to determine if a topic should be built based on changed files in latest commit
should_build_topic() {
    local input_path="$1"
    local remote_pdf_path="$2"
    echo "::group::Check if topic should be built (PDF does not exist or input changed)"
    echo "::notice::should_build_topic called with:"
    echo "::notice::  input_path: $input_path"
    echo "::notice::  remote_pdf_path: $remote_pdf_path"
    echo "::notice::  CHANGED_FILES_CSV: $CHANGED_FILES_CSV"
    echo "::notice::  CHANGED_FILES array: ${CHANGED_FILES[*]}"
    # If no changed files are specified, always build
    if [ -z "$CHANGED_FILES_CSV" ]; then
        echo "::notice::  No changed files specified, will build."
        echo "::endgroup::"
        return 0
    fi
    for changed in "${CHANGED_FILES[@]}"; do
        echo "::notice::    Checking changed file: $changed"
        if [[ "$input_path" == *"$changed"* ]] || [[ "$changed" == *"$input_path"* ]]; then
            echo "::notice::    Match found: $input_path <-> $changed"
            echo "::endgroup::"
            return 0
        fi
    done
    # If not in changed files, check if PDF exists on remote
    if remote_pdf_exists "$remote_pdf_path"; then
        echo "::notice::  PDF exists on remote, skipping build."
        echo "::endgroup::"
        return 1
    else
        echo "::notice::  PDF does not exist on remote, will build."
        echo "::endgroup::"
        return 0
    fi
}

# This script is POSIX-compatible and works on macOS (Bash 3.x), Ubuntu, and Zsh.

# Define array of document classes and their toggle positions
# uncomment the following two lines and comment the two lines after if you want to compile documents of a selected documentclass only
# classes=("beamer") # document classes
# toggles=("3")                # documentclass toggles
classes=("book" "book" "article" "beamer") # document classes
toggles=("0" "0" "1" "3")                  # documentclass toggles

class_commands=(
    "\\\\documentclass[a4paper,11pt,svgnames,oneside]{book}"
    "\\\\documentclass[a4paper,11pt,svgnames,exerciseonly,oneside]{book}"
    "\\\\documentclass[svgnames,hyphens]{article}"
    # "\\\\documentclass[11pt,addpoints,svgnames]{exam}"
    "\\\\documentclass[xcolor={table,dvipsnames,svgnames},hyphens]{beamer}"
)

# Topics and their input files for each document class (as flat arrays: topic:path)
book_topics=(
    # Grundlagenfach Informatik
    "Programmieren:Grundlagen_Info/00_Programmieren/Skript/Skript.tex"
    "Zahlendarstellungen_und_Kodierungen:Grundlagen_Info/01_TheoretischeInformatik/Skript/Skript.tex"
    "Kryptologie:Grundlagen_Info/03_Kryptologie/Skript/Skript.tex"
    "Kompression:Grundlagen_Info/04_Kompression/Skript.tex"
    "Datenintegrität:Grundlagen_Info/05_Datenintegritaet/Skript/Skript"
    "Datenbanken:Grundlagen_Info/06_Datenbanken/Skript/Skript.tex"
    "Netzwerke:Grundlagen_Info/07_Netzwerke/Skript/Skript.tex"
    "Tabellenkalkulation:Grundlagen_Info/09_Tabellenkalkulation/skript_tabellenkalkulation.tex"
    "Aus_Daten_Lernen:Grundlagen_Info/10_Aus_Daten_Lernen/Skript/Skript.tex"
    
    # Ergänzungsfach Informatik
    "Endliche_Automaten:EF/Endliche_Automaten/skript_EA.tex"
    "Induktion_und_Rekursion:EF/Induktion_und_Rekursion/skript_induktion_rekursion.tex"
    "Randomisierte_Algorithmen:Grundlagen_Info/01_TheoretischeInformatik/Randomisierte_Algorithmen/Skript/Skript.tex"
    "Kolmogorov-Komplexitaet:EF/Kolmogorov/skript_kolmogorov.tex"

    # Geographie
    "Stadtgeografie:Geografie/Stadtgeografie/Skript/Skript.tex"
    "Geomorphologie:Geografie/Geomorphologie/Skript/Skript.tex"
)

article_topics=(
    # Grundlagenfach Informatik
    "Excel-Projekte:Grundlagen_Info/06_Datenbanken/Excel-Projekte"
    "HannahFry:Grundlagen_Info/08_Gesellschaft/HannahFry"
    "Vertiefungsthema:Grundlagen_Info/08_Gesellschaft/Vertiefungsthema"

    # Ergänzungsfach Informatik
    "Ergaenzungsfach_Ausschreibungstext:EF/Ausschreibung/ausschreibungstext.tex"

    # Various
    "Semesterplanung:Grundlagen_Info/Various/Semesterplanung"
    "Benotung:Grundlagen_Info/Various/Benotung"
    "MA_Thesis_Guidelines:Various/MA Thesis/MA Thesis Guidelines.tex"
    "Filme:Various/Filme.tex"
    "Tabu:Various/Tabu.tex"
    "Fun_Quotes:Various/Fun_Quotes"
)

beamer_topics=(
    # Grundlagenfach Informatik
    "K01Intro:Grundlagen_Info/00_Programmieren/Slides/K01Intro"
    "K01aZeichenketten:Grundlagen_Info/00_Programmieren/Slides/K01aZeichenketten"
    "K02aDefinitionen:Grundlagen_Info/00_Programmieren/Slides/K02aDefinitionen"
    "K02bAnimationen:Grundlagen_Info/00_Programmieren/Slides/K02bAnimationen"
    "K03aParameter:Grundlagen_Info/00_Programmieren/Slides/K03aParameter"
    "K03bVariablen:Grundlagen_Info/00_Programmieren/Slides/K03bVariablen"
    "K03cZeitTabellen:Grundlagen_Info/00_Programmieren/Slides/K03cZeitTabellen"
    "K03dInput:Grundlagen_Info/00_Programmieren/Slides/K03dInput"
    "K04aFunktionenEinzelne:Grundlagen_Info/00_Programmieren/Slides/K04aFunktionenEinzelne"
    "K04bFunktionenMehrere:Grundlagen_Info/00_Programmieren/Slides/K04bFunktionenMehrere"
    "K04zModulo:Grundlagen_Info/00_Programmieren/Slides/K04zModulo"
    "K05aIfElifElse:Grundlagen_Info/00_Programmieren/Slides/K05aIfElifElse"
    "K05bLogischeOperatoren:Grundlagen_Info/00_Programmieren/Slides/K05bLogischeOperatoren"
    "K05cNegation:Grundlagen_Info/00_Programmieren/Slides/K05cNegation"
    "K05dBreakWhile:Grundlagen_Info/00_Programmieren/Slides/K05dBreakWhile"
    "K06aListen:Grundlagen_Info/00_Programmieren/Slides/K06aListen"
    "K06bBubbleSort:Grundlagen_Info/00_Programmieren/Slides/K06bBubbleSort"
    "K06cBinarySearch:Grundlagen_Info/00_Programmieren/Slides/K06cBinarySearch"
    "K06dListenTeil2:Grundlagen_Info/00_Programmieren/Slides/K06dListenTeil2"
    "K06dListenTeil2:Grundlagen_Info/00_Programmieren/Slides/K06eDictionaries"
    "K07Klassen:Grundlagen_Info/00_Programmieren/Slides/K07Klassen"
    "TurtleGrafik:Grundlagen_Info/00_Programmieren/Slides/TurtleGrafik"
    "Zahlensysteme_L01:Grundlagen_Info/01_TheoretischeInformatik/Slides/Zahlensysteme_L01"
    "Zahlensysteme_L02:Grundlagen_Info/01_TheoretischeInformatik/Slides/Zahlensysteme_L02"
    "Zahlensysteme_L03:Grundlagen_Info/01_TheoretischeInformatik/Slides/Zahlensysteme_L03"
    "Zahlensysteme_L04:Grundlagen_Info/01_TheoretischeInformatik/Slides/Zahlensysteme_L04"
    "Zahlensysteme_L05:Grundlagen_Info/01_TheoretischeInformatik/Slides/Zahlensysteme_L05"
    "Graphen_L01:Grundlagen_Info/02_Graphen/Graphen_L01"
    "Graphen_L02:Grundlagen_Info/02_Graphen/Graphen_L02"
    "Graphen_L03:Grundlagen_Info/02_Graphen/Graphen_L03"
    "AbstraktionDurchGraphen_Kapitel01:Grundlagen_Info/02_Graphen/AbstraktionDurchGraphen/Slides_Kapitel01"
    "AbstraktionDurchGraphen_Kapitel02:Grundlagen_Info/02_Graphen/AbstraktionDurchGraphen/Slides_Kapitel02"
    "Kryptologie_L01:Grundlagen_Info/03_Kryptologie/Slides/Kryptologie_L01"
    "Kryptologie_L01prog:Grundlagen_Info/03_Kryptologie/Slides/Kryptologie_L01prog"
    "L02a_Kryptoanalyse_Caesar:Grundlagen_Info/03_Kryptologie/Slides/L02a_Kryptoanalyse_Caesar"
    "L02b_Kryptoanalyse_Monoalph:Grundlagen_Info/03_Kryptologie/Slides/L02b_Kryptoanalyse_Monoalph"
    "L02c_Kryptoanalyse_Vigenere:Grundlagen_Info/03_Kryptologie/Slides/L02c_Kryptoanalyse_Vigenere"
    "L02d_Kryptoanalyse_Vigenere_Friedman:Grundlagen_Info/03_Kryptologie/Slides/L02d_Kryptoanalyse_Vigenere_Friedman"
    "L02e_Kryptoanalyse_Vigenere_Kasiski:Grundlagen_Info/03_Kryptologie/Slides/L02e_Kryptoanalyse_Vigenere_Kasiski"
    "Appendix:Grundlagen_Info/03_Kryptologie/Slides/Appendix"
    "Kompression_L01_Intro:Grundlagen_Info/04_Kompression/Slides/Kompression_L01_Intro"
    "Kompression_L02_MaxBal:Grundlagen_Info/04_Kompression/Slides/Kompression_L02_MaxBal"
    "Kompression_L03_Huffman:Grundlagen_Info/04_Kompression/Slides/Kompression_L03_Huffman"
    "Kompression_L04_Arithm:Grundlagen_Info/04_Kompression/Slides/Kompression_L04_Arithm"
    "01_Intro:Grundlagen_Info/05_Datenintegritaet/Slides/01_Intro"
    "02_Fehlererkennung:Grundlagen_Info/05_Datenintegritaet/Slides/02_Fehlererkennung"
    "03_Fehlerkorrektur:Grundlagen_Info/05_Datenintegritaet/Slides/03_Fehlerkorrektur"
    "04_Kartentrick:Grundlagen_Info/05_Datenintegritaet/Slides/04_Kartentrick"
    "05_RAID:Grundlagen_Info/05_Datenintegritaet/Slides/05_RAID"
    "01_Slides_Intro:Grundlagen_Info/06_Datenbanken/Slides/01_Slides_Intro"
    "02_Slides_SELECT:Grundlagen_Info/06_Datenbanken/Slides/02_Slides_SELECT"
    "02b_Slides_Subqueries:Grundlagen_Info/06_Datenbanken/Slides/02b_Slides_Subqueries"
    "03_Slides_JOIN:Grundlagen_Info/06_Datenbanken/Slides/03_Slides_JOIN"
    "04_Slides_DML:Grundlagen_Info/06_Datenbanken/Slides/04_Slides_DML"
    "05_Slides_Game:Grundlagen_Info/06_Datenbanken/Slides/05_Slides_Game"
    "Netzwerke_L00:Grundlagen_Info/07_Netzwerke/Slides/00_Netzwerke_Geschichte"
    "Netzwerke_L01:Grundlagen_Info/07_Netzwerke/Slides/01_Netzwerke_Intro" 
    "correlation_causation:Grundlagen_Info/10_Aus_Daten_Lernen/Slides/correlation_causation"
    "linear_regression:Grundlagen_Info/10_Aus_Daten_Lernen/Slides/linear_regression"
    "markov_chains:Grundlagen_Info/10_Aus_Daten_Lernen/Slides/markov_chains"
    "markov_appendix:Grundlagen_Info/10_Aus_Daten_Lernen/Slides/markov_appendix"

    # Ergänzungsfach Informatik
    "complexity:EF/Complexity/complexity"
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
        echo "::warning:: No topics defined for $class, skipping..."
        continue
    fi

    for entry in "${topics[@]}"; do
        topic="${entry%%:*}"
        input_path="${entry#*:}"
        # Extract LEVEL as the first directory in input_path
        LEVEL=$(echo "$input_path" | cut -d'/' -f1)
        # Determine output directory and file names, distinguishing between book variants
        if [ "$class" = "book" ]; then
            # Check if this is the exerciseonly variant
            if echo "$class_command" | grep -q "exerciseonly"; then
                book_variant="exerciseonly"
                latex_dir="${root_dir}/PDFs/${LEVEL}/${topic}/${class}_${book_variant}/"
                output_file="${root_dir}/output_${class}_${book_variant}_${topic// /_}.tex"
            else
                book_variant="solutions"
                latex_dir="${root_dir}/PDFs/${LEVEL}/${topic}/${class}_${book_variant}/"
                output_file="${root_dir}/output_${class}_${book_variant}_${topic// /_}.tex"
            fi
        elif [ "$class" != "book" ]; then
            # Group by main topic after Grundlagen_Info/ for beamer
            if [ "$class" = "beamer" ]; then
                # Extract main topic (e.g. Programmieren, Theoretische Informatik, etc.)
                main_topic=$(echo "$input_path" | sed -E 's|Grundlagen_Info/([^/]+)/.*|\1|' | sed -E 's/^[0-9_]+//')
                # Convert CamelCase to "Camel Case"
                main_topic=$(echo "$main_topic" | sed -E 's/([a-z])([A-Z])/\1 \2/g')
                # Convert ASCII umlauts to actual umlauts
                main_topic=$(echo "$main_topic" | sed -e 's/ae/ä/g' -e 's/oe/ö/g' -e 's/ue/ü/g' -e 's/Ae/Ä/g' -e 's/Oe/Ö/g' -e 's/Ue/Ü/g')
                latex_dir="${root_dir}/PDFs/${LEVEL}/${main_topic}/beamer/${topic}/"
            else
                latex_dir="${root_dir}/PDFs/${LEVEL}/${class}/${topic}/"
            fi
            output_file="${root_dir}/output_${class}_${topic// /_}.tex"
        else
            latex_dir="${root_dir}/PDFs/${LEVEL}/${topic}/${class}/"
            output_file="${root_dir}/output_${class}_${topic// /_}.tex"
        fi
        mkdir -p "$latex_dir"

        # Print current values for debugging
        echo "::group::Processing entry $entry"
        echo "::notice::Processing entry: $entry"
        echo "::notice::  topic: $topic"
        echo "::notice::  input_path: $input_path"
        echo "::notice::  output_file: $output_file"
        echo "::notice::  output_dir: $latex_dir"

        cp "${root_dir}/main.tex" "$output_file"

        # Replace the document class line
        sed "${SED_INPLACE[@]}" "s/\\\\\documentclass.*{.*}/$class_command/" "$output_file"
        # Replace the document class toggle line
        sed "${SED_INPLACE[@]}" "s/\\\\\def\\\\\documentToggle{[0-9]}/\\\\def\\\\documentToggle{$toggle}/" "$output_file"
        # Replace the topic line (if present)
        sed "${SED_INPLACE[@]}" "s/\\\\newcommand{\\\\thetopic}{.*}/\\\\newcommand{\\\\thetopic}{$topic}/" "$output_file"
        # Uncomment the necessary input line
        sed "${SED_INPLACE[@]}" "s|[[:space:]]*%*[[:space:]]*\\\\input{$input_path}|\\\\input{$input_path}|" "$output_file"

        # Determine expected PDF name and remote path for remote existence check
        pdf_name="$(basename "$output_file" .tex).pdf"
        if [ "$class" = "book" ]; then
            remote_pdf_path="PDFs/${LEVEL}/${topic}/${class}_${book_variant}/$pdf_name"
        elif [ "$class" = "beamer" ]; then
            remote_pdf_path="PDFs/${LEVEL}/${main_topic}/beamer/${topic}/$pdf_name"
        else
            remote_pdf_path="PDFs/${LEVEL}/${class}/${topic}/$pdf_name"
        fi

        # Only build if the topic's input_path matches a changed file or PDF is missing on remote
        should_build_topic "$input_path" "$remote_pdf_path" || continue

        # Create a temporary directory for biber
        mkdir -p ~/tmp_exec
        export TMPDIR=~/tmp_exec

        # Compile for all article classes: lualatex -> biber -> makeglossaries -> lualatex -> lualatex (even if no citations or glossaries are used)
        echo "::notice::  step 1: lualatex"
        lualatex -synctex=1 -interaction=nonstopmode -output-directory="$latex_dir" "$output_file" | grep -E "^(!|l\.)" || true

        echo "::notice::  step 2: biber"
        biber --input-directory="$latex_dir" --output-directory="$latex_dir" "$(basename "$output_file" .tex)"

        echo "::notice::  step 3: makeglossaries"
        makeglossaries -d "$latex_dir" "$(basename "$output_file" .tex)" || true

        echo "::notice::  step 4: lualatex"
        lualatex -synctex=1 -interaction=nonstopmode -output-directory="$latex_dir" "$output_file" | grep -E "^(!|l\.)" || true

        echo "::notice::  step 5: lualatex"
        lualatex -synctex=1 -output-directory="$latex_dir" "$output_file" | grep -E "^(!|l\.)|Warning" || true

        # Check for LaTeX errors in the log file
        log_file="${latex_dir}$(basename "$output_file" .tex).log"
        if grep -q '^!' "$log_file"; then
            echo "::error::LaTeX error detected in $input_path. Aborting."
            # Write error message and all lines starting with '!' from the log file to last_failed_file.txt
            {
                echo "LaTeX error detected in $input_path"
                echo "----------------------------------------"
                cat "$log_file"
            } >"$root_dir/last_failed_file.txt"
            exit 1
        fi

        # Clean up intermediate .tex file
        rm "$output_file"

        # Remove all aux files (but keep log files and PDFs)
        if [ -d "$latex_dir" ]; then
            cd "$latex_dir"
            rm -f *.bcf *.ist *.aux *.xml *.idx *.glo *.toc *.gz *.nav *.snm *vrb *.bbl *.blg *.lot *.lof *.gls *glg
            cd "$root_dir"
        fi

        # Remove any folders in the root directory starting with luatex*
        find "$root_dir" -maxdepth 1 -type d -name 'luatex*' -exec rm -rf {} +

        # Copy all files and folders from PDFs to Cyril's Synology NAS
        if [[ "$OSTYPE" != *darwin* ]]; then
            # Use sshpass to provide the password non-interactively
            sshpass -p "$LEE_TEX_SSH_PASSWORD" rsync -av --chmod=ugo=rwX -e "ssh -p 50037 -o StrictHostKeyChecking=no" "${root_dir}/PDFs/" leetex@51.154.36.16:/volume1/LeeTeX/PDFs/

            if [ $? -ne 0 ]; then
                echo "::error::rsync failed. Aborting."
                exit 1
            fi
        fi

        echo "::endgroup::"
    done
done

echo "::notice::Compilation of all document types complete."
