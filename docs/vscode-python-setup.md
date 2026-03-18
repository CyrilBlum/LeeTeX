---
layout: default
title: VS Code + Python Setup
nav_order: 2
---

# VS Code und Python installieren (Windows und macOS)

Diese Anleitung entspricht den Befehlen und Schritten aus dem Skriptkapitel "Getting Started". Alle Codeblöcke sind direkt kopierbar.

## macOS

### Homebrew installieren

Öffnen Sie das Terminal und führen Sie diesen Befehl aus:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Folgen Sie danach den Hinweisen von Homebrew im Terminal, insbesondere den Befehlen zum Aktualisieren von `PATH`.

### VS Code installieren

```bash
brew install --cask visual-studio-code
```

### Python 3 installieren

```bash
brew install python3
```

### tkinter für turtle installieren

```bash
brew install python-tk
```

Falls VS Code beim ersten Start von macOS blockiert wird, geben Sie die Freigabe in den Systemeinstellungen unter Sicherheit.

## Windows

Öffnen Sie PowerShell als Administrator und führen Sie nacheinander diese Befehle aus:

```powershell
winget install -e --id Microsoft.VisualStudioCode --scope machine --silent --accept-package-agreements --accept-source-agreements
winget install -e --id Python.Python.3.14 --scope machine --silent --accept-package-agreements --accept-source-agreements
```

Wenn beim Einfügen Leerzeichen fehlen, korrigieren Sie die Leerzeichen vor dem Ausführen manuell.

## VS Code für Python einrichten

Installieren Sie in VS Code die Erweiterung `Python` (Microsoft). Sie bringt IntelliSense, Debugging und weitere Python-Funktionen mit.

Erstellen Sie danach eine Datei `hello_world.py` und testen Sie den ersten Lauf mit diesem Inhalt:

```python
print("Hello, World!")
```
