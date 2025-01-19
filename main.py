import os
from functools import wraps

from prepreparation.load_images import load_images
from calculations.compare_images import compare_images
from calculations.match_and_format_metrics import is_match, format_metrics
from image_movement.move_and_rename_images import move_and_rename_image
from image_movement.delete_images import delete_images
from logs.process_logs import logger
from constants.DIR import LR_DIR, HR_DIR, MATCHES_DIR
from thresholds.base_treshold import base_treshold
from tqdm import tqdm


def log_if_enabled(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get('enable_logging'):
            func(*args, **kwargs)

    return wrapper


@log_if_enabled
def log_match(lr_file, hr_file, metrics):
    logger.info(f"{lr_file} и {hr_file} matched. Metrics:\n{format_metrics(metrics)}")


@log_if_enabled
def log_no_match(lr_file, hr_file, metrics):
    logger.info(f"{lr_file} и {hr_file} didn't match. Metrics:\n{format_metrics(metrics)}")


def process_matches(matches, enable_logging):
    for lr_file, hr_file in matches:
        move_and_rename_image(hr_file, MATCHES_DIR, f"{lr_file}_{hr_file}")
        delete_images(lr_file, hr_file)
        if enable_logging:
            log_match(lr_file, hr_file, {})


def main(thresholds=base_treshold, enable_logging=False):
    if not os.path.exists(MATCHES_DIR):
        os.makedirs(MATCHES_DIR)

    lr_images = load_images(LR_DIR)
    hr_images = load_images(HR_DIR)

    total_comparisons = len(lr_images) * len(hr_images)

    pbar = tqdm(total=total_comparisons, leave=False)

    matches = []

    for lr_file, lr_img in lr_images:
        for hr_file, hr_img in hr_images:
            metrics = compare_images(lr_img, hr_img)
            if is_match(metrics, thresholds):
                matches.append((lr_file, hr_file))
            else:
                log_no_match(lr_file, hr_file, metrics)
            pbar.update(1)

    pbar.close()

    process_matches(matches, enable_logging)


main()
