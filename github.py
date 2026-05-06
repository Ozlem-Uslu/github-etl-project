#Bibliotheken importieren
import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

#Bringe Python dazu, die .env-Datei zu lesen.
load_dotenv()

#Token lesen
github_token = os.getenv("GITHUB_TOKEN")

#header erstellen
headers = {
    "Accept": "application/vnd.github+json"          #Dies teilt GitHub Folgendes mit:Sende mir die Antwort im JSON-Format.
}

if github_token:
    headers["Authorization"] = f"Bearer {github_token}"

#eine leere Liste erstellen
all_repo_data = []

#Sucheinstellungen
query = "stars:>1000"
per_page = 100
total_pages = 10

for page in range(1, total_pages + 1):                  #Wir werden also Daten von 10 verschiedenen Seiten von GitHub abrufen.
    url = "https://api.github.com/search/repositories"  #Dies ist der Such-Endpoint für GitHub-Repositorys.

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": per_page,
        "page": page
    }
#API request
    response = requests.get(url, headers=headers, params=params)
#Status code  drucken
    print(f"Page {page} - Status:", response.status_code)
#Fehlerprüfung     
    if response.status_code != 200:      #Das bedeutet:Wenn der Status nicht 200 ist:Fehlermeldung ausgeben, Schleife beenden
        print("Error:", response.text)
        break

    data = response.json()
    repos = data["items"]

    for repo_data in repos:
        clean_data = {                              #transformation
            "repo_name": repo_data["name"],
            "full_name": repo_data["full_name"],
            "owner": repo_data["owner"]["login"],
            "stars": repo_data["stargazers_count"],
            "forks": repo_data["forks_count"],
            "language": repo_data["language"],
            "open_issues": repo_data["open_issues_count"],
            "created_at": repo_data["created_at"],
            "updated_at": repo_data["updated_at"],
            "html_url": repo_data["html_url"]
        }

        all_repo_data.append(clean_data)
#Wir warten nach jeder Seite 2 Sekunden.
    time.sleep(2)

df = pd.DataFrame(all_repo_data)

df.to_csv("github_top_1000_repos.csv", index=False)

print("\nGesamtzahl der Repositories:", len(df))
print("Eine CSV-Datei wurde erstellt: github_top_1000_repos.csv ✅")