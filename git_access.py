from git import Repo
from github import Github, Auth
import os

def run_clone(repo_name):
    auth = Auth.Token(os.environ.get('GITHUB_TOKEN'))
    g = Github(auth=auth)

    repo = g.get_repo(f"lordbeerus0505/{repo_name}")
    url = repo.clone_url

    Repo.clone_from(url, "local_ai_with_rag")

    os.chdir("local_ai_with_rag")