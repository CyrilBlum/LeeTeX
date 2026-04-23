---
layout: page
title: About
permalink: /about/
---

<div align="center">
	<a href="https://cyrilblum.github.io/LeeTeX/"><img src="Logos/Logo GymForMATeCH Lines.png" alt="GymForMATeCH Logo" width="300"/></a><br>
	<br>
	© Educational Resources<br>
	<br>
</div>

## About

- “Gym” stands for (Swiss) Gymnasium. This project primarily provides open-source teaching materials at upper-secondary level.
- “ymForMaTeCH” stands for the project’s informatics focus.
- “ForM” stands for form, as the teaching materials are intended to meet high formal standards (see [README.md](README.md) and [GitHub Page](https://cyrilblum.github.io/LeeTeX/)).
- “MA” stands for Maturität, but also for meta-analysis, as one goal of this project is to integrate existing teaching materials as effectively as possible.
- “TeCH” stands for LaTeX as the technical foundation of this repository.
- “CH” stands for the Swiss context of this repository.

## Compiling GymForMATeCH

To compile this project, navigate to `main.tex` and chose to run either a `book`, `article`, `exam`, `beamer` or `flashcard` documentclass, using the toggles. Uncomment a line to compile a certain project. 

We recommend running the following **compilation sequences**
- `book`: `lualatex -> biber -> makeglossaries -> lualatex -> lualatex` 
- other document classes: `lualatex -> lualatex`

We recommend using VS Code for modifying the code.

## Add git hash to documents

If you wish to add a git hash to the document, execute the following steps:

- Navigate to the GymForMATeCH root directory
- `cp -a Git_Internal_Files/. .git/hooks`
- `cd .git/hooks/`
- `chmod ug+x post-checkout post-commit post-merge`
- add, commit and push any outstanding changes, then`git checkout`
- In main.tex, change the `showgitinfo2` toggle to `true`

## Contributing
Please let the authors know if you'd like to contribute.

## Terms of use
Please let us know if you'd like to use contents of this project or yourself (see email addresses below).

## Contact
- [Thomas Graf](mailto:thomas.grf@edu.zh.ch), Kantonsschule Im Lee (KST)
- [Cyril Blum](mailto:cyril.blum@edu.zh.ch), Kantonsschule Im Lee (KST), Kantonsschule Stadelhofen Filiale Dübendorf (KSTfDü)
