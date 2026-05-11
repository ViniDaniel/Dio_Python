from fastapi import FastAPI
from datetime import datetime, UTC

app = FastAPI()

fake_db = [
    {"Title": "Filme 1", "Data": datetime.now(UTC)},
    {"Title": "Filme 2", "Data": datetime.now(UTC)},
    {"Title": "Filme 5", "Data": datetime.now(UTC)},
    {"Title": "Filme 4", "Data": datetime.now(UTC)},
    
]

@app.get("/post")
def read_post(skip, limit):
    return fake_db

@app.get("/post/{framework}")
def read_framework_post(framework: str):
    return {"posts" : [{"Title1": f"Criando aplicação em {framework}", "Data": datetime.now(UTC)},
    {"Title2": "Sleep", "Data": datetime.now(UTC)}
    ]}