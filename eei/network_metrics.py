import numpy as np
import scipy.sparse as sp
from typing import Union


class NetworkTopologyMetrics:
    """
    Calculates network metrics and Information Isolation Intensity (σ).
    """

    @staticmethod
    def compute_silo_isolation_intensity(
        adjacency_matrix: np.ndarray,
        silo_partition: np.ndarray
    ) -> float:
        """
        Calculates spatial isolation intensity (σ) based on modularity and cross-silo density.
        
        :param adjacency_matrix: Adjacency matrix of information flow (N x N)
        :param silo_partition: Cluster/Community membership vector for each node
        :return: Isolation Intensity σ (0.0: fully connected, 1.0: completely isolated silos)
        """
        adj = np.asarray(adjacency_matrix, dtype=float)
        num_nodes = adj.shape[0]
        total_edges = np.sum(adj)
        
        if total_edges == 0:
            return 1.0

        # Create mask for intra-silo vs inter-silo links
        partition_matrix = np.equal.outer(silo_partition, silo_partition)
        
        intra_silo_edges = np.sum(adj * partition_matrix)
        inter_silo_edges = total_edges - intra_silo_edges
        
        # Isolation intensity σ is the proportion of information trapped inside local silos
        sigma = intra_silo_edges / total_edges
        return float(np.clip(sigma, 0.0, 1.0))

    @staticmethod
    def compute_effective_path_length(adjacency_matrix: np.ndarray) -> float:
        """
        Estimates cross-silo average path length as an indicator of fragmentation.
        """
        # Replace 0 weights with infinity for path computation
        adj = np.where(adjacency_matrix == 0, np.inf, adjacency_matrix)
        np.fill_diagonal(adj, 0)
        
        # Simple mean connectivity proxy
        valid_connections = adj[np.isfinite(adj)]
        if len(valid_connections) == 0:
            return np.inf
        return float(np.mean(valid_connections))
