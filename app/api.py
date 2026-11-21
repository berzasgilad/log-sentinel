from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.database import get_logs, get_incidents

app = FastAPI()


@app.get("/logs")
def list_logs(limit: int = 100):
    return get_logs(limit)


@app.get("/incidents")
def list_incidents():
    return get_incidents()

@app.get("/", response_class=HTMLResponse)
def dashboard():
    with open("app/dashboard.html", encoding="utf-8") as f:
        return f.read()