from fastapi import FastAPI

from api.shemas import HealthCheck

app = FastAPI()


@app.get("/health-check", response_model=HealthCheck, tags=["Health"])
def health_check():
    return HealthCheck()
