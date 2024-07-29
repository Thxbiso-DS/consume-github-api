# Consume Github API (186)

## Project Overview

* **Objective:** The objective of this project is to consume the GitHub API to fetch pull requests for a specified repository within a given date range.
* **Project Instructions:** [here](http://syllabus.africacode.net/projects/github-api-consume/part1/)

## Prerequisites

- Python 3.x
- [Requests](https://pypi.org/project/requests/): which is in the `requirements.txt` file ready for installation 

## File Structure

```
├── README.md
├── requirements.txt
├── setup.py
└── src
    └── consume_github_api.py
```
## Installation and Setup

1. **Clone this repository to your local machine.**
   ```bash
    git clone https://github.com/Thxbiso-DS/consume-github-api.git
   ```
2. **Navigate to the repo.**
    ```bash
    cd consume-github-api/
    ```
3. **Create a virtual environment:**
    ```bash 
    python -m venv github_api_env
    ```
4. **Activate the virtual environment:**
   - On Windows:
    ```
    .\github_api_env\Scripts\activate
    ```
   - On macOS/Linux:
    ```
    source github_api_env/bin/activate
    ```
5. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
6. **Install the `setup.py` file to import the `get_pull_requests` function as a module**
    ```bash
    pip install -e .
    ```
7. **Set the PYTHONPATH explicitly to include the root directory of the project: Include the path from your home directory to the project directory**
   ```bash
    export PYTHONPATH=/path/from/home/to/Thabiso-Mokgete-186-consume-github-api-python:$PYTHONPATH

   ```
8. **Add GitHub Token:**
   - Generate a GitHub token from your GitHub account settings > Developer settings > Personal access tokens.
   - Set the environment variable GITHUB_TOKEN to the generated token:
        ```bash
        export GITHUB_TOKEN=your_generated_token_here
        ```

### Using the Consume GitHub API Package
1. Import the `consume_git_api` package in your Python scripts or interactive sessions and use the `get_pull_requests` function to get all the pull requests of a specified repo within a given date range.

    ```python
    from consume_github_api import get_pull_requests

    stats_thinking_prs = get_pull_requests(owner="Thxbiso-DS", repo="statistical-thinking", start_date="2024-07-20",  end_date="2024-07-27")
    
    print(stats_thinking_prs)
    ```
2. You can also use the package in interactive Python sessions

## Author 
Thabiso Mokgete  
* s.mokgete@gmail.com

## License 
Copyright © 2024 [Thabiso Mokgete](https://github.com/Thxbiso-DS).<br />
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)