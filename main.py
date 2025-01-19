import os

from prepreparation.load_images import load_images
from calculations.compare_images import compare_images
from calculations.match_and_format_metrics import is_match, format_metrics
from image_movement.move_and_rename_images import move_and_rename_image
from image_movement.delete_images import delete_images
from logs.process_logs import logger
from constants.DIR import LR_DIR, HR_DIR, MATCHES_DIR
from thresholds.base_treshold import base_treshold
from tqdm import tqdm


def main(thresholds=base_treshold, enable_logging=False):
    if not os.path.exists(MATCHES_DIR):
        os.makedirs(MATCHES_DIR)

    lr_images = load_images(LR_DIR)
    hr_images = load_images(HR_DIR)

    total_comparisons = len(lr_images) * len(hr_images)

    pbar = tqdm(total=total_comparisons)

    for lr_file, lr_img in lr_images:
        for hr_file, hr_img in hr_images:
            metrics = compare_images(lr_img, hr_img)

            if is_match(metrics, thresholds):
                if enable_logging:
                    logger.info(f"{lr_file} и {hr_file} matched. Metrics:\n{format_metrics(metrics)}")

                move_and_rename_image(hr_file, MATCHES_DIR, f"{lr_file}_{hr_file}")
                delete_images(lr_file, hr_file)
            elif enable_logging:
                logger.info(f"{lr_file} и {hr_file} didn't match. Metrics:\n{format_metrics(metrics)}")

            pbar.update(1)

    pbar.close()


main()
