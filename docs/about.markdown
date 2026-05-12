---
layout: page
title: About
permalink: /about/
---

<div align="center">
	<img src="../assets/images/Logo FreeFlower.png" alt="FreeFlower Logo" width="300"/><br>
	<br>
	© Educational Resources<br>
	<br>
</div>

## About

FreeFlower is an open-source project providing high-quality teaching materials for Swiss upper-secondary education (Gymnasium) with a focus on informatics. It integrates existing educational resources with a focus on informatics, meeting rigorous formal standards (see [Rules for Contribution](https://cyrilblum.github.io/FreeFlower/zusammenarbeit.html)). Built on LaTeX, this repository aims to support Swiss educational institutions through meta-analysis and effective material integration.

## Compiling FreeFlower

To compile this project, navigate to `main.tex` and chose to run either a `book`, `article`, `exam`, `beamer` or `flashcard` documentclass, using the toggles. Uncomment a line to compile a certain project. 

We recommend running the following **compilation sequences**
- `book`: `lualatex -> biber -> makeglossaries -> lualatex -> lualatex` 
- other document classes: `lualatex -> lualatex`

We recommend using VS Code for modifying the code.

## Add git hash to documents

If you wish to add a git hash to the document, execute the following steps:

- Navigate to the FreeFlower root directory
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
