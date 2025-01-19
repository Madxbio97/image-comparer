import os
import tqdm
from logger import Logger
from DIRS import lr_dir, hr_dir, match_dir
from utils import check_thresholds, move_image
from metrics import compare_images

if __name__ == "__main__":
    logger = Logger()

    for lr_img in tqdm.tqdm(os.listdir(lr_dir)):
        lr_path = os.path.join(lr_dir, lr_img)

        for hr_img in tqdm.tqdm(os.listdir(hr_dir)):
            hr_path = os.path.join(hr_dir, hr_img)

            metrics = compare_images(lr_path, hr_path)
            if check_thresholds(metrics):
                new_hr_name = f"{hr_img[:-4]}_{lr_img}"
                move_image(hr_path, match_dir, new_hr_name)

                os.remove(lr_path)

                logger.log_match(lr_img, hr_img, metrics)
                break
            else:
                logger.log_mismatch(lr_img, hr_img, metrics)

    logger.save_log()
