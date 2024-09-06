from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from starlette.responses import FileResponse

from app.algorithms import kmeans

router = APIRouter()

ALGORITHMS = {
    "kmeans": "Kmeans clustering",
    "birch": "Birch clustering",
    "dbscan": "DBSCAN clustering",
}

DATASETS = {
    "iris": "Iris flower dataset for classification.",
    "wine": "Wine recognition dataset for classification.",
    "breast_cancer": "Breast cancer dataset for classification.",
    "digits": "Handwritten digits dataset for classification.",
}

class Clustering(BaseModel):
    algorithm: str
    dataset: str
    use_pca: bool

@router.post("/cluster")
async def cluster(request: Clustering):
    algorithm = request.algorithm
    dataset = request.dataset
    use_pca = request.use_pca

    if algorithm not in ALGORITHMS:
        raise HTTPException(status_code=404, detail="Algorithm not found")

    if dataset not in DATASETS:
        raise HTTPException(status_code=404, detail="Dataset not found")

    if algorithm == "kmeans":
        plot = kmeans.run(dataset, use_pca)
        return {"file": plot}

    return {"algorithm": algorithm, "dataset": dataset, "use_pca": use_pca}

@router.get("/cluster/algorithms")
async def get_algorithms():
    return {"algorithms": ALGORITHMS}

@router.get("/cluster/dataset")
async def get_dataset():
    return {"dataset": DATASETS}