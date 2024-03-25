![Lee Logo](https://github.com/ThomasGrafNumerics/LeeTeX/blob/main/GrundlagenInfo/DataScience/04_Kompression/Figures/LeeLogo%20300%20dpi.jpg)
<div align="center">
    <h3>LeeTeX</h3>
    <br>
    © Educational Resources<br>
    <br>
</div>

## Overview

LeeTeX collects educational resources sharing a common typesetting setup.

## Compiling LeeTeX

Compile using LuaLaTeX.

## Add git hash to documents

If you wish to add a git hash to the document, execute the following steps:

- Navigate to the LeeTeX root directory
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
[Thomas Graf](mailto:thomas.grf@edu.zh.ch), Kantonsschule Im Lee
[Cyril Wendl](mailto:cyril.wendl@edu.zh.ch), Kantonsschule Im Lee
