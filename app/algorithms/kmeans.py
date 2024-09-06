import pandas as pd
import  matplotlib.pyplot as plt
from pandas.plotting import plot_params
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.datasets import load_wine, load_iris, load_breast_cancer, load_digits

def load_dataset(dataset: str):
    if dataset == 'wine':
        return load_wine()
    elif dataset == 'iris':
        return load_iris()
    elif dataset == "breast_cancer":
        return load_breast_cancer()
    elif dataset == "digits":
        return load_digits()
    else:
        return None


def run(dataset: str, use_pca: bool):
    data = load_dataset(dataset)
    if data is None:
        return None

    df = pd.DataFrame(data.data, columns=data.feature_names)

    # standardize the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)

    # TODO: PCA transformation

    # cluster the data
    knn = KMeans(n_clusters=3, random_state=42)
    labels = knn.fit_predict(X_scaled)

    # plotting the clustered data
    plt.figure(figsize=(8, 6))
    plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis')
    plt.title('K-Means Clustering (Wine Dataset) Without PCA')
    plt.xlabel('Feature 1 (Standardized)')
    plt.ylabel('Feature 2 (Standardized)')
    plt.colorbar(label='Cluster')
    plt.grid(True)

    # save the plot temporarily
    plot_path = '/Users/madeleine/Datateknikk/DTE-2803-BigData/assignment-1/oppgave-1/plots/plot.png'
    plt.savefig(plot_path)
    plt.close()

    return plot_path

