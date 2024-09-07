from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import clustering

app = FastAPI()

origins = [
    'https://clustering-algorithms.vercel.app'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clustering.router)

@app.get("/")
async def root():
    return {"message": "Clustering Algorithms API is up and running!"}

