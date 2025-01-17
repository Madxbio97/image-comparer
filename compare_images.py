import numpy as np
from image_comparison_func import mse, psnr, pixel_similarity, correlation_coefficient


# Основная функция для сравнения изображений
def compare_images(img1, img2):
    img1_data = np.array(img1.convert('RGB')).astype(float)
    img2_data = np.array(img2.convert('RGB')).astype(float)

    metrics = {
        'MSE': mse(img1_data, img2_data),
        'PSNR': psnr(mse(img1_data, img2_data)),
        'Pixel Similarity': pixel_similarity(img1_data, img2_data),
        'Correlation Coefficient': correlation_coefficient(img1_data, img2_data)
    }

    # logger.debug(f'Метрики сравнения для {img1.filename} и {img2.filename}:\n{metrics}')

    return metrics
