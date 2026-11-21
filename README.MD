# Log Sentinel

A small log-monitoring and incident-detection service, built step by step to learn backend development, REST APIs, Git, Docker, and CI/CD.

## How it works
1. A simulated app writes log lines (standing in for a real production service).
2. A parser reads each line and turns it into structured data (timestamp, severity, service).
3. Incident rules check the data for patterns that indicate real problems.
4. Everything is stored in a database.
5. A REST API exposes the data to anything that asks for it.
6. A small dashboard (with an optional AI explanation) shows the result.

## Status
Work in progress.