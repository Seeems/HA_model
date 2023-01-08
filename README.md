# Model für Hausarbeit in "Programmieren mit Python" (DLMDWPMP01)

## Einleitung
Dieser Quellcode ist lediglich für die konkrete Aufgabenstellung der Hausarbeit des Fernstudium-Moduls DLMDWPMP01 vorgesehen.
Die Datengrundlage wird aus den drei CSV Dateien gebildet. Diese Daten werden vom Kurs bereitgestellt.

## Ordnerstruktur
```bash
.
├── HA_model
│   └── logs
│       └── data_manager.log
├── README.md
├── analytics.py
├── config.json
├── data_manager.py
├── database.db
├── exceptions.py
├── files
│   ├── ideal.csv
│   ├── test.csv
│   └── train.csv
├── graph.py
├── logs
│   ├── analytics.log
│   └── data_manager.log
├── main.py
├── model.py
├── setup_logger.py
├── test_data_manager.py
└── test_model.py
```

## Aufbau
Das gesamte Programm ist modular aufgebaut. Es unterscheidet sich in folgende Module:
* Main - Hauptdatei zum Ausführen des Programms
* Data Manager - Enthält eine <ins>Klasse</ins> zum Laden der Daten aus CSV Dateien und Datenbank, Speicherung in Datenbank
* Model - Enthält eine <ins>Klasse</ins> für die Datenverarbeitung wie "Finden der besten idealen Funktionen" und Validierung
* Analytics - Enthält eine <ins>Klasse</ins> zur Analyse der Daten
* Graph - Enthält Methoden zur Darstellung der Datenbank 
* Exceptions - Enthält individuell-programmierte Fehler

Für jede <ins>Klasse</ins> wird eine eigene Log-Datei im Verzeichnis "logs" bereitgestellt. Das ist im Sinne der Skalierbarkeit von Vorteil, da es eine isolierte Betrachtung der spezifischen Informationen je <ins>Klasse</ins> ermöglicht.
