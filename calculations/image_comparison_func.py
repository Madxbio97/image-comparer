import numpy as np
from scipy.stats import pearsonr

# Методы сравнения изображений

'''
MSE (mean squared error) - мера среднего квадратического отклонения между двумя изображениями. 
MSE измеряет сумму квадратических разностей между элементами двух изображений и усредняет эту сумму на число элементов изображения. 
Чем меньше значение MSE, тем больше схожесть изображений.

PSNR (peak signal-to-noise ratio) - оценка степени точности восстановления изображения после компрессии. 
PSNR рассчитывается как отношение максимального значения сигнала к шуму, который появляется при передаче изображения. 
Высокий PSNR свидетельствует о хорошем качестве изображения, низкий PSNR указывает на значительное количество ошибок и искажений.

Pixel similarity - мера совпадания пикселей двух изображений. 
Эта метрика оценивает долю пикселей, которые совпадают между двумя изображениями. 
Чем больше пикселов совпадают, тем сильнее идентичность изображений.

Correlation coefficient - статистический метод оценки связи между двумя массивами данных. 
Correlation coefficient вычисляет коэффициент Пирсона для двумарочных изображений. 
Этот показатель отражает степень линейной зависимости между значениями пикселей двух изображений. 
Высокая коррелировка указывает на высокую вероятность того, что изображения схожи.
'''


def mse(image1, image2):
    err = np.mean((image1 - image2) ** 2)
    return err


def psnr(mse_val):
    if mse_val == 0:
        return float('inf')  # PSNR бесконечен, когда MSE равно нулю
    max_pixel_value = 255.0
    return 20 * np.log10(max_pixel_value / np.sqrt(mse_val))


def pixel_similarity(image1, image2):
    same_pixels = np.sum(np.all(image1 == image2, axis=2))
    total_pixels = image1.shape[0] * image1.shape[1]
    return same_pixels / total_pixels


def correlation_coefficient_optimized(image1, image2):
    flattened1 = image1.ravel()
    flattened2 = image2.ravel()
    corr_coef, _ = pearsonr(flattened1, flattened2)
    return corr_coef
