import os
import errno

from constants.DIR import LR_DIR, HR_DIR
from logs.process_logs import logger


def delete_images(lr_file, hr_file):
    lr_path = os.path.join(LR_DIR, lr_file)
    hr_path = os.path.join(HR_DIR, hr_file)
    try:
        os.remove(lr_path)
        os.remove(hr_path)
    except OSError as e:
        if e.errno == errno.ENOENT:
            logger.warning(
                f"The {hr_file} file has already been deleted from the HR_DIR directory, so the file deletion from LR_DIR continues.")
            logger.info(f"Deleted images: {lr_file}, {hr_file}")
        else:
            logger.error(f"Error when deleting an image {lr_file}: {e}")
