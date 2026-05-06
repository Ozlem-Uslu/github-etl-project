# GitHub ETL Projekt #

Dieses Projekt ist eine einfache Data-Engineering-ETL-Pipeline, die mit Python und der GitHub REST API entwickelt wurde.

# Projektübersicht

Die Pipeline:
1. verbindet sich mit der GitHub REST API
2. sucht nach populären GitHub-Repositories
3. extrahiert Repository-Metadaten
4. transformiert rohe JSON-Daten in strukturierte Tabellen
5. speichert die bereinigten Daten als CSV-Datei

Das Projekt sammelt Daten von bis zu 1000 GitHub-Repositories.

# Verwendete Technologien

* Python
* GitHub REST API
* Requests
* Pandas
* CSV
* Git & GitHub

# Extrahierte Daten

Die Pipeline extrahiert folgende Informationen:

* Repository-Name
* Vollständiger Repository-Name
* Owner
* Stars
* Forks
* Programmiersprache
* Anzahl offener Issues
* Erstellungsdatum
* Letztes Update
* Repository-URL

# Beispielhafter Workflow

GitHub API → JSON → Transformation → Pandas DataFrame → CSV Export

# Output

Die finalen Daten werden gespeichert als:

github_top_1000_repos.csv

# Lernziele

Dieses Projekt wurde erstellt, um folgende Themen zu üben:

* API-Integration
* JSON-Parsing
* Daten-Transformation
* ETL-Konzepte
* Data-Ingestion-Pipelines
* Git/GitHub-Workflow

Autorin
Özlem Uslu
