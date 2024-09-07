# Clustering API

This FastAPI application provides a set of endpoints for running various clustering algorithms using `scikit-learn`. It allows users to perform clustering tasks on different datasets using algorithms such as KMeans, DBSCAN, Birch, and Mean Shift.

## Features

- **Clustering Algorithms**: Run various clustering algorithms including KMeans, DBSCAN, Birch, and Mean Shift.
- **PCA Support**: Optionally use PCA to reduce dimensionality before clustering.

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip`

### Clone the Repository

```bash
git clone https://github.com/madeleinewoodbury/cluster-api.git
cd cluster-api
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Running the API
To start the FastAPI server, use the following command:
```bash
uvicorn main:app --reload
```
This API will be available at `http://127.0.0.1:8000`.

### Endpoints
1. `/`
- **Method:** GET
- **Description:** Test endpoint to check if API is working.
- **Response:**
```json
{
    "message": "Clustering Algorithms API is up and running!"
}
```
2. `/cluster/algorithms`
- **Method:** GET
- **Description:** Gets the available algorithms.
- **Response:**
```json
{
    "algorithms": {
        "birch": "Birch clustering",
        "dbscan": "DBSCAN clustering",
        "kmeans": "Kmeans clustering",
        "mean_shift": "Mean shift clustering"
    }
}
```
3`/cluster/dataset`
- **Method:** GET
- **Description:** Gets the available datasets
- **Response:**
```json
{
    "datasets": {
        "breast_cancer": "Breast cancer dataset",
        "digits": "Handwritten digits dataset.",
        "iris": "Iris flower dataset",
        "wine": "Wine recognition dataset"
    }
}
```
4.`/cluster`
- **Method:** POST
- **Description:** Run clustering algorithm on the provided dataset.
- **Request Body:**
```json
{
  "algorithm": "kmeans",   // Supported algorithms: "kmeans", "dbscan", "birch", "mean_shift"
  "dataset": "breast_cancer", // Name of the dataset to use
  "use_pca": false         // Boolean flag to use PCA
}
```
- **Response:**
```json
{
  "labels": [0, 1, 2, ...], // Cluster labels for each data point
  "data": [[x1, x2], [y1, y2], ...], // Data points (PCA transformed or scaled)
  "feature_names": ["feature1", "feature2", ...] // Names of features (or "PC1", "PC2" for PCA)
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
