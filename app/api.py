from fastapi import FastAPI

from app.database import get_logs, get_incidents

app = FastAPI()


@app.get("/logs")
def list_logs(limit: int = 100):
    return get_logs(limit)


@app.get("/incidents")
def list_incidents():
    return get_incidents()