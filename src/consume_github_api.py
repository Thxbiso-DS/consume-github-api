from datetime import datetime
import requests
import os

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
BASE_GITHUB_API_URL = "https://api.github.com"


def validate_owner_name(owner):
    if not isinstance(owner, str):
        raise TypeError("owner name must be a string")


def validate_repo_name(repo):
    if not isinstance(repo, str):
        raise TypeError("repository name must be a string")


def check_owner_existence(owner):
    user_url = f"{BASE_GITHUB_API_URL}/users/{owner}"
    user_response = requests.get(user_url)

    if user_response.status_code == 404:
        raise ValueError(f"User '{owner}' does not exist on GitHub")


def get_headers():
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    return headers


def check_repo_existence(owner, repo):
    repo_url = f"{BASE_GITHUB_API_URL}/repos/{owner}/{repo}"
    headers = get_headers()
    repo_response = requests.get(repo_url, headers=headers)

    if repo_response.status_code == 404:
        raise ValueError(f"Repository '{repo}' does not exist for owner '{owner}'")


def fetch_pull_requests(owner, repo):
    pull_requests_api_url = f"{BASE_GITHUB_API_URL}/repos/{owner}/{repo}/pulls"
    request_parameters = {"state": "all", "per_page": 100}
    headers = get_headers()

    all_pull_requests = []
    page = 1

    while True:
        request_parameters["page"] = page

        response = requests.get(
            pull_requests_api_url, params=request_parameters, headers=headers
        )

        response.raise_for_status()

        pull_requests = response.json()

        if not pull_requests:
            break

        all_pull_requests.extend(pull_requests)
        page += 1

    return all_pull_requests


def validate_date_string(date_string):
    if not isinstance(date_string, str):
        raise TypeError("Date string must be a string")

    try:
        datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"{date_string} is not a valid date")


def format_date(date_string):
    if date_string:
        return datetime.strptime(date_string[:10], "%Y-%m-%d")
    else:
        return None


def filter_pull_requests(pull_requests, start_date, end_date):
    start_date = format_date(start_date)
    end_date = format_date(end_date)

    filtered_pull_requests = []
    for pr in pull_requests:
        created_at = format_date(pr["created_at"])
        updated_at = format_date(pr["updated_at"])
        merged_at = format_date(pr["merged_at"]) if pr["merged_at"] else None
        closed_at = format_date(pr["closed_at"]) if pr["closed_at"] else None
        if (
            (pr["created_at"] and start_date <= created_at <= end_date)
            or (pr["updated_at"] and start_date <= updated_at <= end_date)
            or (merged_at and start_date <= merged_at <= end_date)
            or (closed_at and start_date <= closed_at <= end_date)
        ):

            filtered_pr = {
                "id": pr["id"],
                "user": pr["user"]["login"],
                "title": pr["title"],
                "state": pr["state"],
                "created_at": created_at.strftime("%Y-%m-%d"),
            }
            filtered_pull_requests.append(filtered_pr)

    return filtered_pull_requests


def get_pull_requests(owner, repo, start_date, end_date):
    validate_owner_name(owner)
    validate_repo_name(repo)
    validate_date_string(start_date)
    validate_date_string(end_date)

    check_owner_existence(owner)
    check_repo_existence(owner, repo)

    pull_requests = fetch_pull_requests(owner, repo)
    filtered_pull_requests = filter_pull_requests(pull_requests, start_date, end_date)

    return filtered_pull_requests

print(get_pull_requests(
  owner="Umuzi-org",
  repo="ACN-syllabus",
  start_date="2024-03-01",
  end_date="2024-03-10"
))