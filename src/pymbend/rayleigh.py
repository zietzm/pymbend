import numpy as np
from numpy.typing import ArrayLike, NDArray

from . import MbendMethod, mbend


def bend_generalized_rayleigh(
    numerator: ArrayLike,
    denominator: ArrayLike,
    numerator_weight: ArrayLike,
    invert_weights: bool = False,
    max_iter: int = 10000,
    small_positive: float = 1e-4,
    tol: float = 1e-5,
) -> NDArray:
    numerator = np.asarray(numerator)
    denominator = np.asarray(denominator)

    cholesky = np.linalg.cholesky(denominator)
    cholesky_inv = np.linalg.inv(cholesky)

    transformed_numerator = cholesky_inv @ numerator @ cholesky_inv.T

    bent_transformed = mbend(
        transformed_numerator,
        numerator_weight,
        invert_weights=invert_weights,
        max_iter=max_iter,
        small_positive=small_positive,
        method=MbendMethod.ZIETZ,
        tol=tol,
    )

    bent_numerator = cholesky @ bent_transformed @ cholesky.T
    return bent_numerator
