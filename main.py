from fastapi import FastAPI
from app.routes import clustering

app = FastAPI()

app.include_router(clustering.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

