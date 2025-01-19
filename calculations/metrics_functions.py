import numpy as np
from scipy.stats import pearsonr


def mse(image1, image2):
    assert image1.shape == image2.shape, "Images must have the same shape."

    image1 = image1.astype(float)
    image2 = image2.astype(float)

    # Вычисляем MSE
    err = np.mean((image1 - image2) ** 2)
    return err


def psnr(mse_val, data_range=None):
    if mse_val == 0:
        return float('inf')  # The PSNR is infinity when the MSE is zero

    if data_range is None:
        data_range = 255.0

    return 20 * np.log10(data_range / np.sqrt(mse_val))


def pixel_similarity(image1, image2):
    assert image1.shape == image2.shape, "Images must have the same shape."

    same_pixels = np.sum(np.allclose(image1, image2, atol=1e-08, rtol=1e-05))

    total_pixels = image1.size

    return same_pixels / total_pixels


def correlation_coefficient_optimized(image1, image2):
    assert image1.shape == image2.shape, "Images must have the same shape."

    image1 = image1.astype(float)
    image2 = image2.astype(float)

    flattened1 = image1.ravel()
    flattened2 = image2.ravel()

    try:
        corr_coef, _ = pearsonr(flattened1, flattened2)
    except ValueError:
        if np.std(flattened1) == 0 and np.std(flattened2) == 0:
            corr_coef = 1.0 if np.all(flattened1 == flattened2) else 0.0
        else:
            corr_coef = 0.0

    return corr_coef
