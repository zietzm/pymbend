from enum import Enum

import numpy as np
from numpy.typing import ArrayLike, NDArray


class MbendMethod(Enum):
    JORJANI = "hj"
    SCHAEFFER = "lrs"


def mbend(
    matrix: ArrayLike,
    weights: ArrayLike | None = None,
    invert_weights: bool = False,
    max_iter: int = 10000,
    small_positive: float = 1e-4,
    method: MbendMethod = MbendMethod.JORJANI,
) -> NDArray:
    matrix = np.asarray(matrix)
    check_matrix(matrix)

    weights = process_weights(weights, invert_weights)

    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    i = 0
    while i < max_iter and np.any(eigenvalues < 0):
        match method:
            case MbendMethod.JORJANI:
                eigenvalues[eigenvalues < 0] = small_positive
            case MbendMethod.SCHAEFFER:
                sum_neg = 2 * eigenvalues[eigenvalues < 0].sum()
                denom = 1 + 100 * sum_neg**2
                small_positive = eigenvalues[eigenvalues > 0].min()
                eigenvalues[eigenvalues < 0] = (
                    small_positive
                    * np.square(sum_neg - eigenvalues[eigenvalues < 0])
                    / denom
                )
                transformed = eigenvectors @ np.diag(eigenvalues) @ eigenvectors.T
                eigenvalues = np.linalg.eigvalsh(transformed)
                eigenvalues[eigenvalues < 0] = small_positive / 10

        transformed = eigenvectors @ np.diag(eigenvalues) @ eigenvectors.T
        diff = matrix - transformed
        if weights is not None:
            diff = diff * weights
        matrix -= diff

        eigenvalues, eigenvectors = np.linalg.eigh(matrix)
        i += 1

    return matrix


def check_matrix(matrix: NDArray) -> None:
    if matrix.ndim != 2:
        raise ValueError("matrix must be 2-dimensional")
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("matrix must be square")
    if not np.allclose(matrix, matrix.T):
        raise ValueError("matrix must be symmetric")


def process_weights(weights: ArrayLike | None, invert_weights: bool) -> NDArray | None:
    if weights is None:
        return None

    weights = np.asarray(weights)
    check_matrix(weights)

    if invert_weights:
        weights = invert_weight_matrix(weights)

    weights = weights / weights.max()
    return np.asarray(weights)


def invert_weight_matrix(weights: NDArray) -> NDArray:
    weights[weights != 0] = 1 / weights[weights != 0]
    return weights
