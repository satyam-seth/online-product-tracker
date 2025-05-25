from fastapi import FastAPI

from app.schemas import HealthCheck

app = FastAPI()


@app.get("/health-check", response_model=HealthCheck, tags=["Health"])
def health_check():
    return HealthCheck()
