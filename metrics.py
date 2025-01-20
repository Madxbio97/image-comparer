import cv2
from skimage.metrics import structural_similarity as ssim
from scipy.stats import pearsonr
import numpy as np
import warnings


def mse(image_a, image_b):
    err = np.sum((image_a.astype("float") - image_b.astype("float")) ** 2)
    err /= float(image_a.shape[0] * image_a.shape[1])
    return err


def psnr(mse_value):
    if mse_value == 0:
        return float('inf')
    else:
        return 20 * np.log10(255 / np.sqrt(mse_value))


def pixel_similarity(image_a, image_b):
    return np.mean(np.equal(image_a, image_b)) * 100


def correlation_coefficient_optimized(image_a, image_b):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        corr_coef = pearsonr(image_a.flatten(), image_b.flatten())
        if np.isnan(corr_coef[0]):
            return 0.0
        else:
            return corr_coef[0]


def compare_images(image_a, image_b):
    metrics = {}

    image_a = cv2.cvtColor(cv2.imread(image_a), cv2.COLOR_BGR2GRAY)
    image_b = cv2.cvtColor(cv2.imread(image_b), cv2.COLOR_BGR2GRAY)

    metrics['MSE'] = mse(image_a, image_b)
    metrics['PSNR'] = psnr(metrics['MSE'])
    metrics['SSIM'] = ssim(image_a, image_b)
    metrics['pixel_similarity'] = pixel_similarity(image_a, image_b)
    metrics['correlation_coefficient_optimized'] = correlation_coefficient_optimized(image_a, image_b)

    return metrics
