from fastapi import FastAPI
from app.api.v1.routes.extract import router

app = FastAPI(title="Vision OCR to Excel")
app.include_router(router)

@app.get("/")
def root():
    return {"status": "ok"}
