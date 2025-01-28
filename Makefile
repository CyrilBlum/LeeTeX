# Main document file (without .tex extension)
MAIN := main
BUILD_DIR := build

# LaTeX compiler and options
LATEX := lualatex
LATEX_FLAGS := -interaction=nonstopmode -shell-escape -output-directory=$(BUILD_DIR)

# Bibliography compiler
BIBTEX := biber

# Dependency tracking files
DEP_FILES := $(wildcard $(BUILD_DIR)/*.tex.d)

# PDF output
PDF := $(BUILD_DIR)/$(MAIN).pdf

# Source directory for .tex files
SRC_DIR := .
SRC_FILES := $(wildcard $(SRC_DIR)/*.tex)

.PHONY: all clean view help indent

# Default target
all: $(PDF)

# Rule to generate the main PDF
$(PDF): $(SRC_DIR)/$(MAIN).tex $(DEP_FILES) | $(BUILD_DIR)
	$(LATEX) $(LATEX_FLAGS) $(SRC_DIR)/$(MAIN).tex
	if [ -f $(BUILD_DIR)/$(MAIN).bcf ]; then $(BIBTEX) $(BUILD_DIR)/$(MAIN); fi
	$(LATEX) $(LATEX_FLAGS) $(SRC_DIR)/$(MAIN).tex
	$(LATEX) $(LATEX_FLAGS) $(SRC_DIR)/$(MAIN).tex

# Rule for creating .tex dependency files
$(BUILD_DIR)/%.tex.d: $(SRC_DIR)/%.tex | $(BUILD_DIR)
	@mkdir -p $(BUILD_DIR)
	$(LATEX) $(LATEX_FLAGS) -draftmode -recorder $< >/dev/null
	@awk '/^INPUT/ { print "$(BUILD_DIR)/" $$2 ": $<" }' $(BUILD_DIR)/$(MAIN).fls > $@

# Ensure build directory exists
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

# Clean up intermediate and output files
clean:
	rm -rf $(BUILD_DIR)

# View the final PDF
view: $(PDF)
	zathura $(PDF) &

# Indent .tex files using latexindent
indent:
	latexindent -w -m -l myindent.yaml $(SRC_FILES)

# Help target
help:
	@echo "Available targets:"
	@echo "  all       - Build the PDF document"
	@echo "  clean     - Remove intermediate files"
	@echo "  view      - Open the PDF with a viewer"
	@echo "  indent    - Reformat .tex files in the 'src' directory using latexindent"
	@echo "  help      - Show this help message"

# Include dependency files (if they exist)
-include $(DEP_FILES)
