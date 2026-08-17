"""
NumPy-powered Linear Algebra & Array Engine.
"""

from typing import List, Tuple
import numpy as np


class MatrixEngine:
    """Handles matrix arithmetic, determinants, inverses, eigenvalues, and transformations."""

    @staticmethod
    def parse_matrix(matrix_str: str) -> np.ndarray:
        """Parses rows separated by ';' and elements by ',' (e.g., '1,2; 3,4')."""
        try:
            rows = [list(map(float, row.strip().split(","))) for row in matrix_str.split(";")]
            arr = np.array(rows, dtype=float)
            if len(set(len(r) for r in rows)) > 1:
                raise ValueError("All rows must have equal number of elements.")
            return arr
        except Exception as e:
            raise ValueError(f"Invalid matrix format. Use '1,2; 3,4'. Error: {e}")

    @staticmethod
    def parse_vector(vector_str: str) -> np.ndarray:
        """Parses comma-separated elements (e.g., '1, 2, 3, 4')."""
        try:
            return np.array(list(map(float, vector_str.split(","))), dtype=float)
        except Exception as e:
            raise ValueError(f"Invalid vector format. Use '1, 2, 3'. Error: {e}")

    @staticmethod
    def add(A: np.ndarray, B: np.ndarray) -> np.ndarray:
        if A.shape != B.shape:
            raise ValueError(f"Shape mismatch: {A.shape} vs {B.shape}")
        return np.add(A, B)

    @staticmethod
    def multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
        return np.matmul(A, B)

    @staticmethod
    def determinant(A: np.ndarray) -> float:
        if A.shape[0] != A.shape[1]:
            raise ValueError("Matrix must be square (N x N) for determinant.")
        return round(float(np.linalg.det(A)), 6)

    @staticmethod
    def inverse(A: np.ndarray) -> np.ndarray:
        if A.shape[0] != A.shape[1]:
            raise ValueError("Matrix must be square (N x N) for inverse.")
        if np.isclose(np.linalg.det(A), 0.0):
            raise ValueError("Singular matrix: Inverse does not exist (det = 0).")
        return np.round(np.linalg.inv(A), 6)

    @staticmethod
    def transpose(A: np.ndarray) -> np.ndarray:
        return np.transpose(A)

    @staticmethod
    def eigenvalues(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        if A.shape[0] != A.shape[1]:
            raise ValueError("Matrix must be square (N x N) for eigenvalues.")
        vals, vecs = np.linalg.eig(A)
        return np.round(vals, 4), np.round(vecs, 4)

    @staticmethod
    def solve_linear_system(A: np.ndarray, B: np.ndarray) -> np.ndarray:
        """Solves A * x = B."""
        return np.round(np.linalg.solve(A, B), 6)

    @staticmethod
    def vector_stats(v: np.ndarray) -> dict:
        return {
            "mean": round(float(np.mean(v)), 4),
            "std": round(float(np.std(v)), 4),
            "variance": round(float(np.var(v)), 4),
            "norm (magnitude)": round(float(np.linalg.norm(v)), 4),
            "sum": round(float(np.sum(v)), 4),
        }
