import requests
import pandas as pd

repos = [
    ("pandas-dev", "pandas"),
    ("microsoft", "vscode"),
    ("facebook", "react"),
    ("tensorflow", "tensorflow"),
    ("apache", "spark"),
    ("keras-team", "keras"),
    ("numpy", "numpy"),
    ("pallets", "flask"),
    ("django", "django"),
    ("scikit-learn", "scikit-learn")
]

all_repo_data = []

for owner, repo in repos:

    url = f"https://api.github.com/repos/{owner}/{repo}"

    headers = {
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers) #exrahieren

    print(f"\nFetching: {owner}/{repo}")
    print("Status:", response.status_code)

    repo_data = response.json()

    clean_data = {
        "repo_name": repo_data["name"],
        "full_name": repo_data["full_name"],
        "stars": repo_data["stargazers_count"],
        "forks": repo_data["forks_count"],
        "language": repo_data["language"],
        "open_issues": repo_data["open_issues_count"]
    }

    all_repo_data.append(clean_data)        #transformieren

print("\nFINAL DATA:\n")

for repo in all_repo_data:
    print(repo)

 #LOAD   

df = pd.DataFrame(all_repo_data)

print("\nDATAFRAME:\n")
print(df)

df.to_csv("github_repos.csv", index=False)

print("\nCSV ist bereit: github_repos.csv ✅")