from fastapi import FastAPI

app = FastAPI(title="Camipatas API")


@app.get("/health")
def health():
    return {"status": "ok"}
