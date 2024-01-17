<div align="center">
    <h3>LeeTeX</h3>
    <br>
    free educational resources
    <br>
</div>

## Overview

LeeTeX collects educational resources sharing a common typesetting setup.


## Contributing


## Compiling LeeTeX

Compile using LuaLaTeX.

## Add git hash to documents

If you wish to add a git hash to the document, execute the following steps:

- Navigate to the LeeTeX root directory
- `cp -a Git\ Internal\ Files/. .git/hooks`
- `cd .git/hooks/`
- `chmod g+x post-checkout post-commit post-merge`
- add, commit and push any outstanding changes, then`git checkout`
- In main.tex, change the `showgitinfo2` toggle to `true`

## Terms of use
