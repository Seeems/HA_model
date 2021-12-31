# Model für Hausarbeit in "Programmieren mit Python" (DLMDWPMP01)

## Einleitung
Dieser Quellcode ist lediglich für die konkrete Aufgabenstellung der Hausarbeit des Fernstudium-Moduls DLMDWPMP01 vorgesehen.
Die Datengrundlage wird aus den drei CSV Dateien gebildet. Diese Daten werden vom Kurs bereitgestellt.

## Ordnerstruktur
```bash
.
├── README.md
├── config.json
├── data_manager.py
├── files
│   ├── ideal.csv
│   ├── test.csv
│   └── train.csv
├── logs
│   └── data_manager.log
├── main.py
├── setup_logger.py
└── test.db
```

## Aufbau
Das gesamte Programm ist modular aufgebaut. Es unterscheidet sich in folgende Module:
* Main - Hauptdatei zum Ausführen des Programms
* Data Manager - Laden der Daten aus CSV Dateien und Datenbank, Speicherung in Datenbank

Für jedes einzelne Modul wird eine eigene Log-Datei im Verzeichnis "logs" bereitgestellt. Das ist im Sinne der Skalierbarkeit von Vorteil, da es eine isolierte Betrachtung der spezifischen Informationen je Modul ermöglicht.