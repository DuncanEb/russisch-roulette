# Struktur: 

## Verzeichnisübersicht

- **russisch-roulette/**
  - **app/** *(Hauptapplikationscode)*
    - `__init__.py` *(Macht app zu einem Python-Package)*
    - `game.py` *(Kernlogik des Spiels)*
    - `revolver.py` *(Revolver-Klasse)*
    - `utils.py` *(Hilfsfunktionen)*
    - `routes.py` *(Web-Endpoints, z. B. für Flask)*
  - **templates/** *(HTML-Dateien für die Web-App)*
    - `index.html` *(Hauptseite des Spiels)*
  - **static/** *(Statische Dateien wie CSS/JS/Images)*
    - **css/**
      - `style.css` *(CSS für Styling)*
    - **js/**
      - `script.js` *(JS für interaktive Elemente)*
    - **images/** *(Bilder)*
  - **tests/** *(Tests für deine Anwendung)*
    - `test_game.py` *(Testet die Spiellogik)*
  - `main.py` *(Einstiegspunkt der Anwendung)*
  - `requirements.txt` *(Abhängigkeiten, z. B. Flask)*
  - `README.md` *(Dokumentation)*

## Beschreibung der Verzeichnisse und Dateien

### `app/`
Enthält den Hauptapplikationscode:
- **`__init__.py`**: Macht das Verzeichnis zu einem Python-Package.
- **`game.py`**: Enthält die Kernlogik des Spiels.
- **`revolver.py`**: Definiert die Revolver-Klasse.
- **`utils.py`**: Enthält Hilfsfunktionen.
- **`routes.py`**: Definiert die Web-Endpunkte (z. B. für Flask).

### `templates/`
HTML-Dateien für die Web-App:
- **`index.html`**: Die Hauptseite des Spiels.

### `static/`
Beinhaltet statische Dateien wie CSS, JavaScript und Bilder:
- **`css/`**: Enthält Stylesheets (z. B. `style.css` für das Styling).
- **`js/`**: Enthält JavaScript-Dateien (z. B. `script.js` für interaktive Elemente).
- **`images/`**: Enthält Bilder.

### `tests/`
Testfälle für die Anwendung:
- **`test_game.py`**: Testet die Spiellogik.

### Wurzelverzeichnis
- **`main.py`**: Einstiegspunkt der Anwendung, um die App zu starten.
- **`requirements.txt`**: Listet Abhängigkeiten auf (z. B. Flask).
- **`README.md`**: Dokumentation des Projekts.
