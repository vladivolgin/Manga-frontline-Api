from fastapi import FastAPI
from app.api import manga_router
from app.config import settings

app = FastAPI(title="Manga API")

app.include_router(manga_router, prefix=settings.API_V1_STR)

# switch server host address according to environment
def getHost():
    if settings.ENV and settings.ENV=='docker':
        return "0.0.0.0"
    return "127.0.0.1"

@app.get("/")
def root():
    return {"message": "Welcome to Manga API"}

if __name__ == "__main__":
       import uvicorn
       uvicorn.run(app, host=getHost(), port=8000)
