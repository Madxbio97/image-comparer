import numpy as np
from scipy.stats import pearsonr


def compare_images(img1, img2):
    img1_data = np.asarray(img1.convert('RGB'), dtype=np.float32)
    img2_data = np.asarray(img2.convert('RGB'), dtype=np.float32)

    mse_value = ((img1_data - img2_data) ** 2).mean(axis=None)

    max_pixel_value = 255.0
    psnr_value = 20 * np.log10(max_pixel_value / np.sqrt(mse_value)) if mse_value != 0 else float('inf')

    flattened_img1 = img1_data.flatten()
    flattened_img2 = img2_data.flatten()
    corr_coeff, _ = pearsonr(flattened_img1, flattened_img2)

    similarity = np.sum(np.abs(img1_data - img2_data) <= 1) / img1_data.size

    metrics = {
        'MSE': mse_value,
        'PSNR': psnr_value,
        'Pixel Similarity': similarity,
        'Correlation Coefficient': corr_coeff
    }

    return metrics
