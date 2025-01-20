import os
import tqdm
from concurrent.futures import ThreadPoolExecutor
from logger import Logger
from DIRS import lr_dir, hr_dir, match_dir
from utils import check_thresholds, move_image
from metrics import compare_images


def get_unique_filename(filename, directory):
    base, ext = os.path.splitext(filename)
    counter = 1
    while True:
        new_filename = f"{base}_{counter}{ext}"
        if not os.path.exists(os.path.join(directory, new_filename)):
            return new_filename
        counter += 1


def process_hr_images(lr_img, hr_dir, logger):
    lr_path = os.path.join(lr_dir, lr_img)

    with ThreadPoolExecutor() as executor:
        futures = []
        for hr_img in os.listdir(hr_dir):
            hr_path = os.path.join(hr_dir, hr_img)
            future = executor.submit(compare_images, lr_path, hr_path)
            futures.append((future, hr_img))

        for future, hr_img in futures:
            metrics = future.result()
            if check_thresholds(metrics):
                new_hr_name = f"{hr_img[:-4]}_{lr_img}"
                unique_new_hr_name = get_unique_filename(new_hr_name, match_dir)
                move_image(hr_path, match_dir, unique_new_hr_name)

                os.remove(lr_path)

                logger.log_match(lr_img, hr_img, metrics)
                break
            else:
                logger.log_mismatch(lr_img, hr_img, metrics)


if __name__ == "__main__":
    logger = Logger()

    for lr_img in tqdm.tqdm(os.listdir(lr_dir)):
        process_hr_images(lr_img, hr_dir, logger)

    logger.save_log()
