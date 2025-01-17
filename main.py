import os
from load_images import load_images
from compare_images import compare_images
from match_and_format_metrics import is_match
from match_and_format_metrics import format_metrics
from move_and_rename_images import move_and_rename_image
from delete_images import delete_images
from process_logs import logger
from CONSTANTS import LR_DIR, HR_DIR, MATCHES_DIR

# Главная функция
def main(thresholds=None):
    if thresholds is None:
        thresholds = {
            'MSE': (0, 1000),
            'PSNR': (8, float('inf')),
            'Pixel Similarity': (0.0000, 1.0),
            'Correlation Coefficient': (0.8, 1.0)
        }

    # Создаем директорию для совпадений, если она еще не существует
    if not os.path.exists(MATCHES_DIR):
        os.makedirs(MATCHES_DIR)

    # Загружаем изображения из обеих директорий
    lr_images = load_images(LR_DIR)
    hr_images = load_images(HR_DIR)

    # Сравниваем каждое изображение из LR с каждым из HR
    for lr_file, lr_img in lr_images:
        for hr_file, hr_img in hr_images:
            metrics = compare_images(lr_img, hr_img)
            if is_match(metrics, thresholds):
                logger.info(f"{lr_file} и {hr_file} совпали. Метрики:\n{format_metrics(metrics)}")
                move_and_rename_image(hr_file, MATCHES_DIR, f"{lr_file}_{hr_file}")
                delete_images(lr_file, hr_file)
            else:
                logger.info(f"{lr_file} и {hr_file} не совпали. Метрики:\n{format_metrics(metrics)}")


# Запуск основной функции
main()
