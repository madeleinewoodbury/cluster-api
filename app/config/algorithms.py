from enum import Enum
from sklearn.cluster import KMeans, Birch, DBSCAN, MeanShift

class AlgorithmType(Enum):
    BIRCH = 'birch'
    DBSCAN = 'dbscan'
    KMEANS = 'kmeans'
    MEAN_SHIFT = 'mean_shift'

class AlgorithmList:
    def __init__(self):
        self.algorithms = {
            AlgorithmType.BIRCH: "Birch clustering",
            AlgorithmType.DBSCAN: "DBSCAN clustering",
            AlgorithmType.KMEANS: "Kmeans clustering",
            AlgorithmType.MEAN_SHIFT: "Mean shift clustering"
        }

    def contains(self, name) -> bool:
        for algorithm in self.algorithms:
            if name == algorithm.value:
                return True

    def get_cluster_model(self, algorithm: str):
        if not self.contains(algorithm):
            return None

        if algorithm == AlgorithmType.BIRCH.value:
            return Birch(n_clusters=3)
        if algorithm == AlgorithmType.DBSCAN.value:
            return DBSCAN(eps=1.0, min_samples=5)
        if algorithm == AlgorithmType.KMEANS.value:
            return KMeans(n_clusters=3)
        if algorithm == AlgorithmType.MEAN_SHIFT.value:
            return MeanShift()

        return None


algorithms = AlgorithmList()