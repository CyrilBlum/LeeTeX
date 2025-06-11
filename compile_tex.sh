#!/bin/bash
# At the top of compile_tex.sh
LEE_TEX_SSH_PASSWORD="$1"

# This script is POSIX-compatible and works on macOS (Bash 3.x), Ubuntu, and Zsh.

# Define array of document classes and their toggle positions
# classes=("book" "book" "article" "exam", "beamer") # document classes
# toggles=("0" "0" "1" "3")                # documentclass toggles
classes=("book" "book" "article" "beamer") # document classes
toggles=("0" "0" "1" "3")                # documentclass toggles

class_commands=(
    "\\\\documentclass[a4paper,11pt,svgnames,oneside]{book}"
    "\\\\documentclass[a4paper,11pt,svgnames,exerciseonly,oneside]{book}"
    "\\\\documentclass[svgnames,hyphens]{article}"
    # "\\\\documentclass[11pt,addpoints,svgnames]{exam}"
    "\\\\documentclass[xcolor={table,dvipsnames,svgnames},hyphens]{beamer}"
)

# Topics and their input files for each document class (as flat arrays: topic:path)
book_topics=(
    # OInf topics
    "Programmieren:Grundlagen_Info/00_Programmieren/Skript/Skript.tex"
    "Zahlendarstellungen_und_Kodierungen:Grundlagen_Info/01_TheoretischeInformatik/Skript/Skript.tex"
    "Randomisierte_Algorithmen:Grundlagen_Info/01_TheoretischeInformatik/Randomisierte_Algorithmen/Skript/Skript.tex"
    "Kryptologie:Grundlagen_Info/03_Kryptologie/Skript/Skript.tex"
    "Kompression:Grundlagen_Info/04_Kompression/Skript.tex"
    "Datenintegrität:Grundlagen_Info/05_DatenIntegritaet/Skript/Skript"
    "Datenbanken:Grundlagen_Info/06_Datenbanken/Skript/Skript.tex"
    "Netzwerke:Grundlagen_Info/07_Netzwerke/Skript.tex"
    "Tabellenkalkulation:Grundlagen_Info/09_Tabellenkalkulation/skript_tabellenkalkulation.tex"
    "Aus_Daten_Lernen:Grundlagen_Info/10_Aus_Daten_lernen/Skript/Skript.tex"
    # Cyril Geography topics
    "Stadtgeografie:Geografie/Stadtgeografie/Skript/Skript.tex"
    "Geomorphologie:Geografie/Geomorphologie/Skript/Skript.tex"
    # Thomas EF topics
    "Endliche_Automaten:EF/Endliche_Automaten/skript_EA.tex"
    "Induktion_und_Rekursion:EF/Induktion_und_Rekursion/skript_induktion_rekursion.tex"
    # "Kolmogorov-Komplexitaet:EF/Kolmogorov/skript_kolmogorov.tex"
)

article_topics=(
    # "mwe:LaTeX_related/mwe.tex"
    # "ausschreibungstext:EF/Ausschreibung/ausschreibungstext.tex"
    # "Eingabe_Projektidee:Interessenwochen/Wn_Gf_Sommer_2024/Eingabe_Projektidee"
    # "Auftrag:Interessenwochen/Wn_Gf_Sommer_2024/Auftrag"
    # "Semesterplanung:Grundlagen_Info/Various/Semesterplanung"
    # "Benotung:Grundlagen_Info/Various/Benotung"
    # "Excel-Projekte:Grundlagen_Info/06_Datenbanken/Excel-Projekte"
    # "HannahFry:Grundlagen_Info/08_Gesellschaft/HannahFry"
    # "Feedback:Grundlagen_Info/08_Gesellschaft/Feedback"
    # "Vertiefungsthema:Grundlagen_Info/08_Gesellschaft/Vertiefungsthema"
    # "Lernziele:Grundlagen_Info/10_Aus_Daten_lernen/Lernziele"
    # "Klassentag2024_1c:Various/Klassenstunde/Klassentag2024_1c.tex"
    # "Packliste_Lager:Various/Klassenstunde/Packliste_Lager.tex"
    # "MA_Thesis_Guidelines:Various/MA Thesis/MA Thesis Guidelines.tex"
    # "Filme:Various/Filme.tex"
    # "Keyboard_Shortcuts:Various/Keyboard Shortcuts.tex"
    # "Tabu:Various/Tabu.tex"
    # "Namensschilder:Various/Namensschilder"
    # "Provokante_Aussagen:Various/Provokante_Aussagen"
    # "Fun_Quotes:Various/Fun_Quotes"
    "Unterrichtsvorbereitung:Private/PHBern/3 BPA/Unterrichtsvorbereitung.tex"
)

beamer_topics=(
    # # Topics marked with # # currently have issues compiling and need to be reviewed.
    "K01Intro:Grundlagen_Info/00_Programmieren/Slides/K01Intro"
    "K01aZeichenketten:Grundlagen_Info/00_Programmieren/Slides/K01aZeichenketten"
    "K02aDefinitionen:Grundlagen_Info/00_Programmieren/Slides/K02aDefinitionen"
    "K02bAnimationen:Grundlagen_Info/00_Programmieren/Slides/K02bAnimationen"
    "K03aParameter:Grundlagen_Info/00_Programmieren/Slides/K03aParameter"
    "K03bVariablen:Grundlagen_Info/00_Programmieren/Slides/K03bVariablen"
    "K03cZeitTabellen:Grundlagen_Info/00_Programmieren/Slides/K03cZeitTabellen"
    "K03dInput:Grundlagen_Info/00_Programmieren/Slides/K03dInput"
    "K04aIfElifElse:Grundlagen_Info/00_Programmieren/Slides/K04aIfElifElse"
    "K04bLogischeOperatoren:Grundlagen_Info/00_Programmieren/Slides/K04bLogischeOperatoren"
    "K04cNegation:Grundlagen_Info/00_Programmieren/Slides/K04cNegation"
    "K04dBreakWhile:Grundlagen_Info/00_Programmieren/Slides/K04dBreakWhile"
    "K04zModulo:Grundlagen_Info/00_Programmieren/Slides/K04zModulo"
    "K05aListen:Grundlagen_Info/00_Programmieren/Slides/K05aListen"
    "K05bBubbleSort:Grundlagen_Info/00_Programmieren/Slides/K05bBubbleSort"
    "K05cBinarySearch:Grundlagen_Info/00_Programmieren/Slides/K05cBinarySearch"
    "K05dListenTeil2:Grundlagen_Info/00_Programmieren/Slides/K05dListenTeil2"
    "K07aFunktionenEinzelne:Grundlagen_Info/00_Programmieren/Slides/K07aFunktionenEinzelne"
    "K07bFunktionenMehrere:Grundlagen_Info/00_Programmieren/Slides/K07bFunktionenMehrere"
    "TurtleGrafik:Grundlagen_Info/00_Programmieren/TurtleGrafik"
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
    "01_Intro:Grundlagen_Info/05_DatenIntegritaet/Slides/01_Intro"
    "02_Fehlererkennung:Grundlagen_Info/05_DatenIntegritaet/Slides/02_Fehlererkennung"
    "03_Fehlerkorrektur:Grundlagen_Info/05_DatenIntegritaet/Slides/03_Fehlerkorrektur"
    "04_Kartentrick:Grundlagen_Info/05_DatenIntegritaet/Slides/04_Kartentrick"
    "05_RAID:Grundlagen_Info/05_DatenIntegritaet/Slides/05_RAID"
    "01_Slides_Intro:Grundlagen_Info/06_Datenbanken/Slides/01_Slides_Intro"
    "02_Slides_SELECT:Grundlagen_Info/06_Datenbanken/Slides/02_Slides_SELECT"
    "02b_Slides_Subqueries:Grundlagen_Info/06_Datenbanken/Slides/02b_Slides_Subqueries"
    "03_Slides_JOIN:Grundlagen_Info/06_Datenbanken/Slides/03_Slides_JOIN"
    "04_Slides_DML:Grundlagen_Info/06_Datenbanken/Slides/04_Slides_DML"
    "05_Slides_Game:Grundlagen_Info/06_Datenbanken/Slides/05_Slides_Game"
    "Netzwerke_L01:Grundlagen_Info/07_Netzwerke/Netzwerke_L01"
    "correlation_causation:Grundlagen_Info/10_Aus_Daten_lernen/Slides/correlation_causation.tex"
    "linear_regression:Grundlagen_Info/10_Aus_Daten_lernen/Slides/linear_regression.tex"
    "markov_chains:Grundlagen_Info/10_Aus_Daten_lernen/Slides/markov_chains.tex"
    "markov_appendix:Grundlagen_Info/10_Aus_Daten_lernen/Slides/markov_appendix.tex"
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
            # Group by main topic after Grundlagen_Info/ for beamer
            if [ "$class" = "beamer" ]; then
                # Extract main topic (e.g. Programmieren, Theoretische Informatik, etc.)
                main_topic=$(echo "$input_path" | sed -E 's|Grundlagen_Info/([^/]+)/.*|\1|' | sed -E 's/^[0-9_]+//')
                # Convert CamelCase to "Camel Case"
                main_topic=$(echo "$main_topic" | sed -E 's/([a-z])([A-Z])/\1 \2/g')
                # Convert ASCII umlauts to actual umlauts
                main_topic=$(echo "$main_topic" | sed -e 's/ae/ä/g' -e 's/oe/ö/g' -e 's/ue/ü/g' -e 's/Ae/Ä/g' -e 's/Oe/Ö/g' -e 's/Ue/Ü/g')
                latex_dir="${root_dir}/PDFs/${main_topic}/beamer/${topic}/"
            else
                latex_dir="${root_dir}/PDFs/${class}/${topic}/"
            fi
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
            lualatex -synctex=1 -interaction=nonstopmode -output-directory="$latex_dir" "$output_file" | grep -E "^(!|l\.)" || true

            echo "  step 5: lualatex"
            lualatex -synctex=1 -output-directory="$latex_dir" "$output_file" | grep -E "^(!|l\.)|Warning" || true
        else
            # Double pass for other classes, show only warnings/errors
            echo "  step 1: lualatex"
            lualatex -synctex=1 -interaction=nonstopmode -output-directory="$latex_dir" "$output_file" | grep -E "^(!|l\.)" || true
            echo "  step 2: lualatex"
            lualatex -synctex=1 -output-directory="$latex_dir" "$output_file" | grep -E "^(!|l\.)|Warning" || true
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

        # Remove any folders in the root directory starting with luatex*
        find "$root_dir" -maxdepth 1 -type d -name 'luatex*' -exec rm -rf {} +

        # Copy all files and folders from PDFs to Cyril's Synology NAS
        if [[ "$OSTYPE" != *darwin* ]]; then
            # Use sshpass to provide the password non-interactively (not recommended for security reasons)
            sshpass -p "${LEE_TEX_SSH_PASSWORD}" rsync -av --chmod=ugo=rwX -e "ssh -p 50037" "${root_dir}/PDFs/" leetex@51.154.36.16::LeeTeX/PDFs
            if [ $? -ne 0 ]; then
                echo "rsync failed. Aborting."
                exit 1
            fi
        fi
    done
done

echo "Compilation of all document types complete."
