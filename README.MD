# Log Sentinel

![CI](https://github.com/berzasgilad/log-sentinel/actions/workflows/ci.yml/badge.svg)

A small log-monitoring and incident-detection service: it watches application log lines, detects
incidents with custom-built rules, stores everything in a database, exposes it over a REST API,
and shows it on a live web dashboard.

Built as a personal learning project to practice backend development, REST APIs, SQL, Git,
automated testing, Docker, and CI/CD.

## How it works

1. A simulated app writes log lines (standing in for a real production service).
2. A parser reads each line and turns it into structured data (timestamp, severity, service).
3. Incident rules check the data for patterns that indicate real problems (e.g. repeated errors
   from the same service within a short time window).
4. Everything is stored in an SQLite database.
5. A REST API (FastAPI) exposes the data to anything that asks for it.
6. A small web dashboard shows logs and incidents live, with color-coded severities.

## Tech stack

Python, FastAPI, SQLite, pytest, Docker, GitHub Actions (CI).

## Running locally

\`\`\`bash
python -m venv .venv
.venv\\Scripts\\activate        # Windows
pip install -r requirements.txt

python -m app.generator        # in one terminal: generates log data
python -m app.database         # parses app.log, detects incidents, saves to sentinel.db
uvicorn app.api:app --reload   # starts the API + dashboard at http://127.0.0.1:8000
\`\`\`

## Running with Docker

\`\`\`bash
docker build -t log-sentinel .
docker run -p 8000:8000 log-sentinel
\`\`\`

## Running tests

\`\`\`bash
python -m pytest
\`\`\`