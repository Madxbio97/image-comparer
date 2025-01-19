import os
import cv2
import numpy as np

from constants.DIR import LR_DIR, HR_DIR


def mse(image_a, image_b):
    # Mean Squared Error
    err = np.sum((image_a.astype("float") - image_b.astype("float")) ** 2)
    err /= float(image_a.shape[0] * image_a.shape[1])
    return err


def psnr(mse_value):
    # Peak Signal-to-Noise Ratio
    if mse_value == 0:
        return float('inf')
    else:
        return 20 * np.log10(255 / np.sqrt(mse_value))


def pixel_similarity(image_a, image_b):
    # Pixel similarity based on L1 norm
    diff = np.abs(image_a.astype("int16") - image_b.astype("int16"))
    total_diff = np.sum(diff)
    max_diff = image_a.size * 255
    sim = 1 - (total_diff / max_diff)
    return sim


def correlation_coefficient(image_a, image_b):
    # Pearson's correlation coefficient
    a_flat = image_a.flatten()
    b_flat = image_b.flatten()
    corr_coef = np.corrcoef(a_flat, b_flat)[0, 1]
    return corr_coef


def compare_images(lr_dir, hr_dir):
    lr_files = sorted(os.listdir(lr_dir))
    hr_files = sorted(os.listdir(hr_dir))

    metrics = {
        'MSE': [],
        'PSNR': [],
        'Pixel Similarity': [],
        'Correlation Coefficient': []
    }

    for lr_file in lr_files:
        lr_path = os.path.join(lr_dir, lr_file)
        lr_image = cv2.imread(lr_path, cv2.IMREAD_GRAYSCALE)

        for hr_file in hr_files:
            hr_path = os.path.join(hr_dir, hr_file)
            hr_image = cv2.imread(hr_path, cv2.IMREAD_GRAYSCALE)

            # Calculate metrics
            current_mse = mse(lr_image, hr_image)
            current_psnr = psnr(current_mse)
            current_pixel_sim = pixel_similarity(lr_image, hr_image)
            current_corr_coef = correlation_coefficient(lr_image, hr_image)

            print(f'Comparing {lr_file} with {hr_file}:')
            print(f'MSE: {current_mse:.6f}')
            print(f'PSNR: {current_psnr:.6f}')
            print(f'Pixel Similarity: {current_pixel_sim:.6f}')
            print(f'Correlation Coefficient: {current_corr_coef:.6f}\n')

            # Store values for later statistics
            metrics['MSE'].append(current_mse)
            metrics['PSNR'].append(current_psnr)
            metrics['Pixel Similarity'].append(current_pixel_sim)
            metrics['Correlation Coefficient'].append(current_corr_coef)

    # Calculate overall statistics
    for metric_name, values in metrics.items():
        mean_val = np.mean(values)
        min_val = np.min(values)
        max_val = np.max(values)

        print(f'{metric_name} Statistics:')
        print(f'- Mean: {mean_val:.6f}')
        print(f'- Min: {min_val:.6f}')
        print(f'- Max: {max_val:.6f}\n')


if __name__ == "__main__":
    lr_dir = LR_DIR
    hr_dir = HR_DIR
    compare_images(lr_dir, hr_dir)
