# Weather-Guru

Ein intelligenter Wetter-Assistent, der mithilfe von KI (GPT-4o-mini) Wetterfragen zu deiner Region beantwortet.

## Überblick

Weather-Guru kombiniert Echtzeit-Wetterdaten von der Open-Meteo API mit der Intelligenz von OpenAI's GPT-4o-mini, um als virtueller Meteorologe und Wetterjournalist zu fungieren. Stelle beliebige Fragen zum aktuellen Wetter und erhalte professionelle, verständliche Antworten.

## Features

- Echtzeit-Wetterdaten über Open-Meteo API
- KI-gestützte Wetteranalyse und -beratung mit GPT-4o-mini
- Professionelle, journalistische Antworten
- Deutsche Wetterbeschreibungen
- Responsive Terminal-Ausgabe
- Aktuelle Daten: Temperatur, Wetter-Code, Niederschlagswahrscheinlichkeit

## Technologie-Stack

- **Python 3.13**
- **OpenAI GPT-4o-mini** - KI-Modell für natürlichsprachige Antworten
- **Open-Meteo API** - Kostenlose Wetter-API
- **requests** - HTTP-Anfragen
- **python-dotenv** - Umgebungsvariablen-Management

## Installation

1. Repository klonen oder herunterladen:
```bash
git clone <repository-url>
cd gpt_weather
```

2. Virtuelle Umgebung erstellen und aktivieren:
```bash
python -m venv .venv
source .venv/bin/activate  # Auf Windows: .venv\Scripts\activate
```

3. Dependencies installieren:
```bash
pip install -r requirements.txt
```

4. `.env`-Datei erstellen und OpenAI API-Key eintragen:
```bash
echo "GPT_API_KEY=sk-dein-openai-api-key-hier" > .env
```

## Verwendung

Starte die Anwendung:
```bash
python main.py
```

Das Programm:
1. Zeigt eine Willkommensnachricht
2. Fragt nach deiner Wetter-Frage
3. Ruft aktuelle Wetterdaten ab
4. Lässt GPT die Frage als Meteorologe beantworten

Beispiel-Fragen:
- "Soll ich heute einen Regenschirm mitnehmen?"
- "Wie wird das Wetter in den nächsten Stunden?"
- "Ist es heute kälter als gestern?"
- "Brauche ich eine Jacke?"

## Projektstruktur

```
gpt_weather/
├── main.py                 # Hauptanwendung
├── src/
│   ├── __init__.py
│   └── gpt.py             # OpenAI API Integration
├── data/
│   └── weather_code.json  # Wetter-Code Übersetzungen
├── requirements.txt       # Python Dependencies
├── .env                   # API-Keys (nicht im Repo)
├── .gitignore
└── README.md
```

## Konfiguration

### API-Keys

Du benötigst einen OpenAI API-Key:
1. Registriere dich bei [OpenAI](https://platform.openai.com/)
2. Erstelle einen API-Key im Dashboard
3. Trage den Key in die `.env`-Datei ein

### Standort ändern

Standardmäßig wird das Wetter für Köln/Berlin (Koordinaten: 52.52°N, 13.41°E) abgerufen. Um den Standort zu ändern, bearbeite die Koordinaten in `main.py:26`:

```python
res = requests.get('https://api.open-meteo.com/v1/forecast?latitude=DEIN_BREITENGRAD&longitude=DEIN_LÄNGENGRAD&...')
```

## Wetter-Codes

Das Projekt verwendet standardisierte WMO-Wetter-Codes (0-99), die in `data/weather_code.json` in deutsche Beschreibungen übersetzt werden:

- 0: Klarer Himmel
- 1-3: Bewölkung
- 45-48: Nebel
- 51-67: Regen/Nieselregen
- 71-77: Schneefall
- 80-86: Schauer
- 95-99: Gewitter

## Roadmap / Zukünftige Features

- [ ] Unterstützung für mehrere Städte
- [ ] 7-Tage-Vorhersage
- [ ] Grafische Darstellung der Wetterdaten
- [ ] Sprachauswahl (Englisch/Deutsch)
- [ ] Wetteralarme und Benachrichtigungen
- [ ] Integration mit weiteren KI-Modellen (Claude, etc.)

## API-Limits

- **Open-Meteo**: Kostenlos, keine Rate-Limits für nicht-kommerzielle Nutzung
- **OpenAI GPT-4o-mini**: Pay-per-use, günstigste Option für Chats

## Fehlerbehebung

### "ModuleNotFoundError: No module named 'requests'"
```bash
pip install -r requirements.txt
```

### "API-Key ungültig"
Überprüfe, ob dein OpenAI API-Key in der `.env`-Datei korrekt eingetragen ist.

### "FileNotFoundError: weather_code.json"
Stelle sicher, dass du das Programm aus dem Projektverzeichnis ausführst.

## Lizenz

Dieses Projekt ist für Bildungszwecke erstellt (Masterschool-Projekt).

## Autor

Bastian Westholt

## Zusätzliche Dateien

Im Projekt befindet sich auch `claude.py` - ein Beispiel-Script für die Integration der Anthropic Claude API, falls du das Projekt auf Claude umstellen möchtest.

---

Made with AI + Weather = Weather-Guru
