import os
from process_logs.logger import Logger
from constants.DIR import lr_dir, hr_dir, match_dir
from modules.compare_images import compare_images
from modules.check_thresholds import check_thresholds
from modules.move_images import move_image
from modules.delete_images import delete_images

if __name__ == "__main__":
    logger = Logger()

    for lr_img in os.listdir(lr_dir):
        lr_path = os.path.join(lr_dir, lr_img)

        for hr_img in os.listdir(hr_dir):
            hr_path = os.path.join(hr_dir, hr_img)

            metrics = compare_images
            if check_thresholds:
                new_hr_name = f"{hr_img[:-4]}_{lr_img}"
                move_image(hr_path, match_dir, new_hr_name)

                delete_images(lr_path)

                logger.log_match(lr_img, hr_img, metrics)
                break
            else:
                logger.log_mismatch(lr_img, hr_img, metrics)

    logger.save_log()
